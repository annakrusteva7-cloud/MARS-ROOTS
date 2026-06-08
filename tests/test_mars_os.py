import pytest
from core_os import MarsProductionOS
from mars_config import MarsConfig

def test_battery_never_negative():
    os = MarsProductionOS(MarsConfig(total_sols=3))
    for _ in range(20):
        os.simulate_climate_cycle()
        os.get_dust_telemetry()
        os.manage_power_grid()
    assert os.power_battery >= 0.0

def test_determinism():
    os1 = MarsProductionOS()
    os2 = MarsProductionOS()
    assert os1.vectorized_monte_carlo() == os2.vectorized_monte_carlo()
