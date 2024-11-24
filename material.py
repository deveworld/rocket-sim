from dataclasses import dataclass


@dataclass
class Material:
    name: str
    uts: int # Ultimate Tensile Strength (Mpa)

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Name cannot be empty")
        if self.uts <= 0:
            raise ValueError("Ultimate Tensile Strength must be greater than 0")


PVC = Material(name="PVC", uts=55)
PLA = Material(name="PLA", uts=40)
AL6061 = Material(name="AL6061", uts=241)