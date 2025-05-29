import math
import re

ENGINEERING_SUFFIXES = {
    'p': 1e-12,
    'n': 1e-9,
    'μ': 1e-6,
    'u': 1e-6,  # allow both μ and u
    'm': 1e-3,
    'k': 1e3,
    'K': 1e3,
    'meg': 1e6,
    'M': 1e6,
    'g': 1e9,
    'G': 1e9,
}


def engineering_str_to_float(s):
    s = s.strip().replace('_', '')
    # Try direct float conversion first
    try:
        return float(s)
    except ValueError:
        pass

    # Regex to separate numeric part and suffix
    match = re.match(r'^([\d.]+)([a-zA-Zμ]*)$', s)
    if not match:
        raise ValueError(f"Invalid engineering notation: '{s}'")

    num_str, suffix = match.groups()
    num = float(num_str)

    if suffix in ENGINEERING_SUFFIXES:
        return num * ENGINEERING_SUFFIXES[suffix]
    else:
        raise ValueError(f"Unknown suffix '{suffix}' in '{s}'")


def to_polar_str(z):
    r = abs(z)
    theta = math.degrees(math.atan2(z.imag, z.real))
    return f"{r:.6g} ∠ {theta:.2f}°"
