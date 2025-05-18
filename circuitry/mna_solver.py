import numpy as np


def resolve_alias(name, aliases):
    # Recursively resolve alias to ultimate node name
    seen = set()
    while name in aliases and name not in seen:
        seen.add(name)
        name = aliases[name]
    return name


def build_mna(components, aliases):
    # Resolve nodes
    for comp in components:
        comp.nodes = [resolve_alias(n, aliases) for n in comp.nodes]

    nodes = set()
    volt_sources = []
    for c in components:
        nodes.update(c.nodes)
        if c.ctype.upper() == 'V':
            volt_sources.append(c)

    ground = resolve_alias('GND', aliases) if 'GND' in aliases else 'GND'
    if ground not in nodes:
        ground = sorted(nodes)[0]

    other_nodes = [n for n in sorted(nodes) if n != ground]
    node_map = {n: i for i, n in enumerate(other_nodes)}

    n = len(other_nodes)
    m = len(volt_sources)

    G = np.zeros((n, n))
    B = np.zeros((n, m))
    C = np.zeros((m, n))
    D = np.zeros((m, m))
    z = np.zeros(n + m)

    v_idx = 0
    for comp in components:
        n1, n2 = comp.nodes
        i = node_map[n1] if n1 != ground else None
        j = node_map[n2] if n2 != ground else None

        if comp.ctype.upper() == 'R':
            g = 1.0 / comp.value
            if i is not None:
                G[i, i] += g
            if j is not None:
                G[j, j] += g
            if i is not None and j is not None:
                G[i, j] -= g
                G[j, i] -= g

        elif comp.ctype.upper() == 'V':
            if i is not None:
                B[i, v_idx] = 1
                C[v_idx, i] = 1
            if j is not None:
                B[j, v_idx] = -1
                C[v_idx, j] = -1
            z[n + v_idx] = comp.value
            v_idx += 1

    A = np.block([[G, B], [C, D]])
    x = np.linalg.solve(A, z)

    return ground, other_nodes, volt_sources, x
