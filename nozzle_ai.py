import numpy as np
from scipy.optimize import brentq

def Pe_P0_Me(Me, gamma):
    return (1 + ((gamma - 1)/2) * Me**2) ** (-gamma / (gamma - 1))

def func_to_solve(Me, gamma, target_Pe_P0):
    return Pe_P0_Me(Me, gamma) - target_Pe_P0

def Ae_Astar(Me, gamma):
    term1 = (1/Me)
    term2 = ((2/(gamma+1))*(1 + ((gamma -1)/2)*Me**2))**((gamma+1)/(2*(gamma -1)))
    return term1 * term2

def main():
    # Given constants
    gamma = 1.137
    R = 8314.46  # J/kmol-K
    M = 39.9  # kg/kmol
    R_specific = R / M  # J/kg-K
    T0 = 1520  # K
    P_ambient_MPa = 0.101325  # MPa

    # Inputs
    F = float(input("Enter target thrust (N): "))
    P0_MPa = float(input("Enter chamber pressure (MPa): "))

    # Convert pressures to Pa
    P0 = P0_MPa * 1e6  # Pa
    P_ambient = P_ambient_MPa * 1e6  # Pa

    # Compute Pe/P0
    Pe_P0 = P_ambient / P0

    # Solve for Me
    target_Pe_P0 = Pe_P0

    # Define Me range
    Me_min = 1.0  # Supersonic flow
    Me_max = 20.0  # Arbitrary upper limit

    Me_solution = brentq(func_to_solve, Me_min, Me_max, args=(gamma, target_Pe_P0))
    Me = Me_solution
    print(f"\nExit Mach number (Me): {Me:.3f}")

    # Compute T_e
    Te_T0 = (1 + ((gamma -1)/2)*Me**2) ** (-1)
    T_e = Te_T0 * T0

    # Compute exit velocity Ve
    Ve = Me * np.sqrt(gamma * R_specific * T_e)
    print(f"Exit velocity (Ve): {Ve:.2f} m/s")

    # Compute mass flow rate mdot
    mdot = F / Ve
    print(f"Mass flow rate (mdot): {mdot:.4f} kg/s")

    # Compute throat area A_throat
    term1 = mdot * np.sqrt(T0)
    term2 = P0 * np.sqrt(gamma / R_specific)
    term3 = ((gamma + 1)/2) ** (- (gamma +1)/(2*(gamma -1)))

    A_throat = term1 / (term2 * term3)
    print(f"Throat area (A_throat): {A_throat:.6e} m^2")

    # Compute throat diameter D_throat
    D_throat = np.sqrt(4 * A_throat / np.pi)
    print(f"Throat diameter (D_throat): {D_throat * 1000:.3f} mm")

    # Compute area ratio Ae/A*
    Ae_Astar_value = Ae_Astar(Me, gamma)
    print(f"Area ratio (Ae/A*): {Ae_Astar_value:.3f}")

    # Compute exit area A_exit
    A_exit = Ae_Astar_value * A_throat
    print(f"Exit area (A_exit): {A_exit:.6e} m^2")

    # Compute exit diameter D_exit
    D_exit = np.sqrt(4 * A_exit / np.pi)
    print(f"Exit diameter (D_exit): {D_exit * 1000:.3f} mm")

if __name__ == "__main__":
    main()
