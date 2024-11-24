import math
from dataclasses import dataclass
from material import Material
from propellant import Propellant

@dataclass
class Motor:
    od: float # Outer Diameter (mm)
    id: float = 0 # Inner Diameter (mm)
    height: float # Height of the chamber (mm)
    safety_factor: int = 10 # Safety Factor
    material: Material # Material of the chamber
    propellant: Propellant # Propellant of the Rocket

    def __post_init__(self):
        if self.od <= 0:
            raise ValueError("Outer Diameter must be greater than 0")
        if self.height <= 0:
            raise ValueError("Height must be greater than 0")
        if self.safety_factor <= 1:
            raise ValueError("Safety Factor must be greater than 0")
        if self.material is None:
            raise ValueError("Material cannot be None")
        if self.propellant is None:
            raise ValueError("Propellant cannot be None")

    def calculate_thickness(
            self,
            P_0: float
        ) -> float:
        """Calculate the thickness of the chamber wall.

        Args:
            P_0 (float): Chamber Pressure (MPa)

        Returns:
            float: Thickness of the chamber wall (mm)
        """
        allowable_stress = self.material.uts / self.safety_factor
        r = self.od / 2
        t = (P_0 * r) / allowable_stress

        self.id = self.od - 2 * t
        return t
    
    def calculate_combustion_area(self):
        """Calculate the combustion area of the motor.

        Returns:
            float: Combustion Area (m^2)
        """
        if self.id == 0:
            raise ValueError("Inner Diameter not calculated")
        
        return self.id * 2 * math.pi * self.height