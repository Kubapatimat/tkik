import math

import numpy as np


def resolve_alias(name, aliases):
    seen = set()
    while name in aliases and name not in seen:
        seen.add(name)
        name = aliases[name]
    return name


def stamp_linear(components, aliases, node_map, ground_idx, n, m):
    """
    Build the linear part of MNA:
      [ G  B ] [v] = [i]
      [ C  D ] [j]   [e]
    Returns A (size (n+m)x(n+m)) and z vector.
    """
    G = np.zeros((n, n))
    B = np.zeros((n, m))
    C = np.zeros((m, n))
    D = np.zeros((m, m))
    z = np.zeros(n + m)

    vs_idx = 0
    for comp in components:
        # nodes after alias resolution
        n1 = node_map.get(resolve_alias(comp.nodes[0], aliases), None)
        n2 = node_map.get(resolve_alias(comp.nodes[1], aliases), None)

        ctype = comp.ctype.upper()
        if ctype == 'R':
            g = 1.0 / comp.value
            if n1 is not None:
                G[n1, n1] += g
            if n2 is not None:
                G[n2, n2] += g
            if n1 is not None and n2 is not None:
                G[n1, n2] -= g
                G[n2, n1] -= g

        elif ctype == 'L':
            # Inductor as short circuit in DC:
            # Large conductance, e.g., 1e9 S
            g = 1e9
            if n1 is not None:
                G[n1, n1] += g
            if n2 is not None:
                G[n2, n2] += g
            if n1 is not None and n2 is not None:
                G[n1, n2] -= g
                G[n2, n1] -= g

        elif ctype == 'C':
            # Capacitor open circuit in DC → no stamp
            pass

        elif ctype == 'V':
            # stamp for voltage source
            if n1 is not None:
                B[n1, vs_idx] = 1
                C[vs_idx, n1] = 1
            if n2 is not None:
                B[n2, vs_idx] = -1
                C[vs_idx, n2] = -1
            z[n + vs_idx] = comp.value
            vs_idx += 1

    A = np.block([[G, B], [C, D]])
    return A, z


def stamp_nonlinear(components, aliases, node_map, ground_idx, x):
    """
    Build residual vector R(x) and Jacobian J(x) for nonlinear stamps
    (e.g. diodes, transistors).
    R & J are size (n+m).
    """
    n_total = len(x)
    R = np.zeros(n_total)
    J = np.zeros((n_total, n_total))

    for comp in components:
        if comp.ctype.upper() == 'D':
            n1 = node_map.get(resolve_alias(comp.nodes[0], aliases), None)
            n2 = node_map.get(resolve_alias(comp.nodes[1], aliases), None)
            v1 = x[n1] if n1 is not None else 0.0
            v2 = x[n2] if n2 is not None else 0.0
            vt = comp.params.get('Vt', 0.02585)
            is_ = comp.value
            vd = v1 - v2
            i_d = is_ * (np.exp(vd / vt) - 1)
            di_d = is_ / vt * np.exp(vd / vt)

            if n1 is not None:
                R[n1] += i_d
                J[n1, n1] += di_d
                if n2 is not None:
                    J[n1, n2] -= di_d
            if n2 is not None:
                R[n2] -= i_d
                if n1 is not None:
                    J[n2, n1] -= di_d
                J[n2, n2] += di_d

    return R, J


def dc_solve(components, aliases, tol=1e-9, max_iter=20):
    # Gather nodes and voltage sources
    all_nodes = set()
    vs_list = []
    for c in components:
        for n in c.nodes:
            all_nodes.add(resolve_alias(n, aliases))
        if c.ctype.upper() == 'V':
            vs_list.append(c)

    # Determine ground node
    ground = resolve_alias('GND', aliases)
    if ground not in all_nodes:
        ground = sorted(all_nodes)[0]

    other_nodes = [n for n in sorted(all_nodes) if n != ground]
    node_map = {node: idx for idx, node in enumerate(other_nodes)}
    n = len(other_nodes)
    m = len(vs_list)

    # Initial guess
    x = np.zeros(n + m)

    for iteration in range(max_iter):
        A, z = stamp_linear(components, aliases, node_map, ground, n, m)
        R, J = stamp_nonlinear(components, aliases, node_map, ground, x)
        res = A @ x - z + R
        jac = A + J

        dx = np.linalg.solve(jac, -res)
        x = x + dx

        if np.linalg.norm(dx) < tol:
            break

    # Compose solution vector: voltages + currents
    solution = x
    return ground, other_nodes, vs_list, solution, node_map, n


def ac_solve(components, aliases, frequency, tol=1e-9, max_iter=20):
    omega = 2 * math.pi * frequency
    all_nodes = set()
    vs_list = []
    for c in components:
        for n in c.nodes:
            all_nodes.add(resolve_alias(n, aliases))
        if c.ctype.upper() == 'V':
            vs_list.append(c)

    ground = resolve_alias('GND', aliases)
    if ground not in all_nodes:
        ground = sorted(all_nodes)[0]

    other_nodes = [n for n in sorted(all_nodes) if n != ground]
    node_map = {node: idx for idx, node in enumerate(other_nodes)}
    n = len(other_nodes)
    m = len(vs_list)

    G = np.zeros((n, n), dtype=complex)
    B = np.zeros((n, m), dtype=complex)
    C = np.zeros((m, n), dtype=complex)
    D = np.zeros((m, m), dtype=complex)
    z = np.zeros(n + m, dtype=complex)

    vs_idx = 0
    for comp in components:
        n1 = node_map.get(resolve_alias(comp.nodes[0], aliases), None)
        n2 = node_map.get(resolve_alias(comp.nodes[1], aliases), None)

        ctype = comp.ctype.upper()
        if ctype == 'R':
            g = 1.0 / comp.value
            if n1 is not None:
                G[n1, n1] += g
            if n2 is not None:
                G[n2, n2] += g
            if n1 is not None and n2 is not None:
                G[n1, n2] -= g
                G[n2, n1] -= g

        elif ctype == 'L':
            z_L = 1j * omega * comp.value
            y_L = 1 / z_L
            if n1 is not None:
                G[n1, n1] += y_L
            if n2 is not None:
                G[n2, n2] += y_L
            if n1 is not None and n2 is not None:
                G[n1, n2] -= y_L
                G[n2, n1] -= y_L

        elif ctype == 'C':
            z_C = 1 / (1j * omega * comp.value)
            y_C = 1 / z_C
            if n1 is not None:
                G[n1, n1] += y_C
            if n2 is not None:
                G[n2, n2] += y_C
            if n1 is not None and n2 is not None:
                G[n1, n2] -= y_C
                G[n2, n1] -= y_C

        elif ctype == 'V':
            if n1 is not None:
                B[n1, vs_idx] = 1
                C[vs_idx, n1] = 1
            if n2 is not None:
                B[n2, vs_idx] = -1
                C[vs_idx, n2] = -1
            z[n + vs_idx] = comp.value
            vs_idx += 1

    A = np.block([[G, B], [C, D]])

    solution = np.linalg.solve(A, z)

    return ground, other_nodes, vs_list, solution, node_map, n


def element_voltage(comp, node_map, ground, solution, aliases):
    n1 = node_map.get(resolve_alias(comp.nodes[0], aliases), None)
    n2 = node_map.get(resolve_alias(comp.nodes[1], aliases), None)

    v1 = solution[n1] if n1 is not None else 0.0
    v2 = solution[n2] if n2 is not None else 0.0
    return v1 - v2


def element_current(comp, node_map, ground, solution, vs_list, n, aliases, omega=None):
    ctype = comp.ctype.upper()

    if ctype == 'V':
        idx = vs_list.index(comp)
        return solution[n + idx]

    n1 = node_map.get(resolve_alias(comp.nodes[0], aliases), None)
    n2 = node_map.get(resolve_alias(comp.nodes[1], aliases), None)

    v1 = solution[n1] if n1 is not None else 0.0
    v2 = solution[n2] if n2 is not None else 0.0
    v_diff = v1 - v2

    if ctype == 'R':
        return v_diff / comp.value

    elif ctype == 'L':
        if omega is None:
            # DC approx short circuit, current = 0
            return 0.0
        else:
            # I = V / (jωL)
            return v_diff / (1j * omega * comp.value)

    elif ctype == 'C':
        if omega is None:
            # DC approx open circuit, current = 0
            return 0.0
        else:
            # I = jωC * V
            return 1j * omega * comp.value * v_diff

    elif ctype == 'D':
        # Approximate diode current from voltage (assuming exponential diode I-V)
        vt = comp.params.get('Vt', 0.02585)
        is_ = comp.value
        return is_ * (math.exp(v_diff / vt) - 1)

    else:
        return None
