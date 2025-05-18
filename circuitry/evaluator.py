import re

unit_multipliers = {
    'f': 1e-15, 'p': 1e-12, 'n': 1e-9, 'u': 1e-6, 'μ': 1e-6,
    'm': 1e-3, '': 1, 'k': 1e3, 'K': 1e3, 'M': 1e6, 'G': 1e9, 'T': 1e12
}


def parse_value(value_str):
    match = re.fullmatch(r'([0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?)([fpnuμmkKMGT]?)', value_str)
    if not match:
        raise ValueError(f"Invalid value format: {value_str}")
    number_str, unit_str = match.groups()
    multiplier = unit_multipliers.get(unit_str, 1)
    return float(number_str) * multiplier
