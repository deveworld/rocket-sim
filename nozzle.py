import math
from dataclasses import dataclass
from motor import Motor

@dataclass
class Nozzle:
    motor: Motor # Motor of the Rocket

    def __post_init__(self):
        if self.motor is None:
            raise ValueError("Motor cannot be None")

    def _calculate_nozzle_throat(
            self,
            P0: float,
            A_b: float,
        ) -> tuple[float, float]:
        """Calculate the Area of Nozzle Throat.

        Args:
            P0 (float): Chamber Pressure (Pa)
            A_b (float): Combustion Area (m^2)

        Returns:
            float: Area of Nozzle Throat (m^2)
            float: Diameter of Nozzle Throat (m)
        """
        R = 8314.3
        k = self.motor.propellant.k
        T0 = self.motor.propellant.T_0
        a = self.motor.propellant.get_a(P0)
        n = self.motor.propellant.get_n(P0)
        rho_p = self.motor.propellant.density * 1000
        
        exponent = (k + 1) / (k - 1)
        term1 = (2 / (k + 1)) ** exponent
        denominator = math.sqrt((k / (R * T0)) * term1)
        D = denominator
        N = D * P0 ** (1 - n)
        A_star = (A_b * a * rho_p) / N
        D_star = 2 * math.sqrt(A_star / math.pi)
        return A_star, D_star
