"""
MARS-ROOTS v4.0: High-Fidelity Martian Physics.
Includes Stefan-Boltzmann dynamics and Solar Insolation modeling.
"""

# Constants based on NASA/SpaceX Martian environmental data
MARS_SOLAR_CONSTANT = 590.0  # W/m2 (Solar intensity on Mars)
EMISSIVITY = 0.85            # Surface property for radiative balance
SIGMA = 5.67e-8              # Stefan-Boltzmann Constant

def calculate_real_heat_loss(temp_celsius):
    """Calculates radiative power loss per unit area."""
    temp_kelvin = temp_celsius + 273.15
    # P = epsilon * sigma * T^4
    power_loss = EMISSIVITY * SIGMA * (temp_kelvin**4)
    return round(power_loss, 2)

if __name__ == "__main__":
    test_temp = -65.0
    loss = calculate_real_heat_loss(test_temp)
    print(f"At {test_temp}C, radiative heat loss is {loss} W/m2.")
