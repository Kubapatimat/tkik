import random

import numpy as np


def to_number(v):
    try:
        return float(v)
    except Exception:
        raise TypeError(f"Cannot convert {v} to number")


def to_int(v):
    try:
        return int(float(v))
    except Exception:
        raise TypeError(f"Cannot convert {v} to int")


def _print(args):
    msg = " ".join(str(v) for v in args.get('_pos', []))
    print(f"[LOG]: {msg}")


def buf(args):
    x = to_number(args.get('_pos', [0])[0])
    return 1 if x > 0.5 else 0


def inv(args):
    x = to_number(args.get('_pos', [0])[0])
    return 0.0 if x > 0.5 else 1.0


def sgn(args):
    x = to_number(args.get('_pos', [0])[0])
    return 1 if x > 0 else (-1 if x < 0 else 0)


def u(args):
    x = to_number(args.get('_pos', [0])[0])
    return 1 if x > 0 else 0


def uramp(args):
    x = to_number(args.get('_pos', [0])[0])
    return x if x > 0 else 0


def d(args):
    pos = args.get('_pos', [])
    if len(pos) == 3:
        f_x, f_x_delta, delta = map(to_number, pos)
        if delta == 0:
            raise ValueError("Delta cannot be zero for derivative")
        return (f_x_delta - f_x) / delta
    else:
        raise ValueError("d() requires exactly 3 positional arguments")


def if_func(args):
    pos = args.get('_pos', [])
    if len(pos) < 3:
        raise ValueError("if(x,y,z) requires three arguments")
    x, y, z = pos[:3]
    return y if to_number(x) > 0.5 else z


def limit(args):
    pos = args.get('_pos', [])
    if len(pos) < 3:
        raise ValueError("limit(x,y,z) requires three arguments")
    x, y, z = map(to_number, pos[:3])
    return max(min(y, z), min(max(y, z), x))


def rand(args):
    x = to_int(args.get('_pos', [0])[0])
    random.seed(x)
    return random.random()


def random_smooth(args):
    # Stub for smooth random: uniform random [0,1]
    return random.uniform(0, 1)


def white(args):
    # Stub for white noise between -0.5 and 0.5
    return random.uniform(-0.5, 0.5)


def table(args):
    pos = args.get('_pos', [])
    if len(pos) < 3 or len(pos) % 2 == 0:
        raise ValueError("table(x,a,b,c,d,...) requires odd number of args >=3")
    x = to_number(pos[0])
    points = list(zip(pos[1::2], pos[2::2]))
    points = [(to_number(a), to_number(b)) for a, b in points]
    points.sort(key=lambda p: p[0])
    if x <= points[0][0]:
        return points[0][1]
    if x >= points[-1][0]:
        return points[-1][1]
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        if x0 <= x <= x1:
            t = (x - x0) / (x1 - x0)
            return y0 * (1 - t) + y1 * t
    return 0


internal_builtins = {
    "print": _print,
    "abs": lambda args: abs(to_number(args.get('_pos', [0])[0])),
    "acos": lambda args: np.arccos(to_number(args.get('_pos', [0])[0])),
    "arccos": lambda args: np.arccos(to_number(args.get('_pos', [0])[0])),
    "acosh": lambda args: np.arccosh(to_number(args.get('_pos', [0])[0])),
    "asin": lambda args: np.arcsin(to_number(args.get('_pos', [0])[0])),
    "arcsin": lambda args: np.arcsin(to_number(args.get('_pos', [0])[0])),
    "asinh": lambda args: np.arcsinh(to_number(args.get('_pos', [0])[0])),
    "atan": lambda args: np.arctan(to_number(args.get('_pos', [0])[0])),
    "arctan": lambda args: np.arctan(to_number(args.get('_pos', [0])[0])),
    "atan2": lambda args: np.arctan2(to_number(args.get('_pos', [1])[0]), to_number(args.get('_pos', [0])[0])),
    "atanh": lambda args: np.arctanh(to_number(args.get('_pos', [0])[0])),
    "buf": buf,
    "ceil": lambda args: np.ceil(to_number(args.get('_pos', [0])[0])),
    "cos": lambda args: np.cos(to_number(args.get('_pos', [0])[0])),
    "cosh": lambda args: np.cosh(to_number(args.get('_pos', [0])[0])),
    "d": d,
    "exp": lambda args: np.exp(to_number(args.get('_pos', [0])[0])),
    "floor": lambda args: np.floor(to_number(args.get('_pos', [0])[0])),
    "hypot": lambda args: np.hypot(to_number(args.get('_pos', [0])[0]), to_number(args.get('_pos', [1])[0])),
    "if": if_func,
    "int": lambda args: to_int(args.get('_pos', [0])[0]),
    "inv": inv,
    "limit": limit,
    "ln": lambda args: np.log(to_number(args.get('_pos', [0])[0])),
    "log": lambda args: np.log(to_number(args.get('_pos', [0])[0])),
    "log10": lambda args: np.log10(to_number(args.get('_pos', [0])[0])),
    "max": lambda args: max(to_number(args.get('_pos', [0])[0]), to_number(args.get('_pos', [1])[0])),
    "min": lambda args: min(to_number(args.get('_pos', [0])[0]), to_number(args.get('_pos', [1])[0])),
    "pow": lambda args: to_number(args.get('_pos', [0])[0]) ** to_number(args.get('_pos', [1])[0]),
    "pwr": lambda args: abs(to_number(args.get('_pos', [0])[0])) ** to_number(args.get('_pos', [1])[0]),
    "pwrs": lambda args: sgn(args) * (abs(to_number(args.get('_pos', [0])[0])) ** to_number(args.get('_pos', [1])[0])),
    "rand": rand,
    "random": random_smooth,
    "round": lambda args: round(to_number(args.get('_pos', [0])[0])),
    "sgn": sgn,
    "sin": lambda args: np.sin(to_number(args.get('_pos', [0])[0])),
    "sinh": lambda args: np.sinh(to_number(args.get('_pos', [0])[0])),
    "sqrt": lambda args: np.sqrt(to_number(args.get('_pos', [0])[0])),
    "table": table,
    "tan": lambda args: np.tan(to_number(args.get('_pos', [0])[0])),
    "tanh": lambda args: np.tanh(to_number(args.get('_pos', [0])[0])),
    "u": u,
    "uramp": uramp,
    "white": white,
}
