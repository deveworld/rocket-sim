from dataclasses import dataclass


@dataclass
class Propellant:
    name: str
    T_0: int # Temperature (K)
    density: float # Density (g/cm^3)
    k: float # Specific Heat Ratio
    M: float # Effective molecular wt. of exhaust products (g/mol=kg/kmol)

    a: dict[tuple[float, float], float] # Pressure Coefficient (m/s/Pa^n) by pressure range
    n: dict[tuple[float, float], float] # Pressure Exponent by pressure range

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Name cannot be empty")
        if self.T_0 <= 0:
            raise ValueError("Temperature must be greater than 0")
        if self.density <= 0:
            raise ValueError("Density must be greater than 0")
        if self.k <= 0:
            raise ValueError("Specific Heat Ratio must be greater than 0")
        if self.M <= 0:
            raise ValueError("Effective molecular wt. of exhaust products must be greater than 0")
        if len(self.a) == 0:
            raise ValueError("Pressure Coefficient cannot be empty")
        if len(self.n) == 0:
            raise ValueError("Pressure Exponent cannot be empty")
    
    def get_a(self, P: float) -> float:
        for key, value in self.a.items():
            if key[0] <= P <= key[1]:
                return value
        raise ValueError(f"a for Pressure {P} not found")

    def get_n(self, P: float) -> float:
        for key, value in self.n.items():
            if key[0] <= P <= key[1]:
                return value
        raise ValueError(f"n for Pressure {P} not found")


KNSB = Propellant(
    name="KNSB",
    T_0=1600,
    density=1.841,
    k=1.137,
    M=39.9,
    a={
        (0.103, 0.779): 8.88,
        (0.779, 2.57): 7.55,
        (2.57, 5.93): 3.84,
        (5.93, 8.50): 17.2,
        (8.50, 11.20): 4.78,
    },
    n={
        (0.103, 0.779): 0.619,
        (0.779, 2.57): -0.009,
        (2.57, 5.93): 0.688,
        (5.93, 8.50): -0.148,
        (8.50, 11.20): 0.442,
    },
)

KNDX = Propellant(
    name="KNDX",
    T_0=1710,
    density=1.879,
    k=1.1308,
    M=42.39,
    a={
        (0.103, 0.807): 10.71,
        (0.807, 1.50): 8.763,
        (1.50, 3.79): 7.852,
        (3.79, 7.03): 3.907,
        (7.03, 10.67): 9.653,
    },
    n={
        (0.103, 0.807): 0.625,
        (0.807, 1.50): -0.314,
        (1.50, 3.79): -0.013,
        (3.79, 7.03): 0.535,
        (7.03, 10.67): 0.064,
    },
)

# KNSU = Propellant(name="KNSU", T_0=1720, k=1.133, M=41.99, a={}, n={})