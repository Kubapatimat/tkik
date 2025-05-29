from dataclasses import dataclass


@dataclass
class Component:
    ctype: str
    name: str
    value: float
    nodes: list[str]
