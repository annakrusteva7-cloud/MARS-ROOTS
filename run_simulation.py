from core_os import MarsProductionOS
from habitat_network import HabitatNetwork
from crop_biomass import CropBiomonitor
from mars_config import MarsConfig
import logging

if __name__ == "__main__":
    logger = logging.getLogger("MarsOS")
    logger.info("=== MARS-ROOTS v6.0.0 FLIGHT-READY ===")

    config = MarsConfig.load()
    os = MarsProductionOS(config)
    crop = CropBiomonitor()
    network = HabitatNetwork(num_habitats=3)

    for sol in range(1, config.total_sols + 1):
        logger.info(f"=== SOL {sol} ===")
        os.simulate_climate_cycle()
        os.get_dust_telemetry()
        os.manage_power_grid()
        crop.monitor_and_irrigate(os)

        survival = os.vectorized_monte_carlo()
        logger.info(f"Battery: {os.power_battery}% | Heater: {os.heater_status} | Survival: {survival}%")

    network.share_resources()
    config.save()
    logger.info("Mission cycle complete. State persisted.")
