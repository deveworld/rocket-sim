from dataclasses import dataclass

@dataclass
class Rocket:
    ds: int
    name: str
    admin: bool = False