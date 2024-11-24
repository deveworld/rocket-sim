from propellant import *


class Database:
    def __init__(self):
        self._propellants = {KNSB, KNDX}

    def get_propellant(self, name: str) -> Propellant:
        for propellant in self._propellants:
            if propellant.name == name:
                return propellant
        raise ValueError(f"Propellant {name} not found")
    