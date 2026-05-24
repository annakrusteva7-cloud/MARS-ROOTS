import logging
from core_os import MarsProductionOS

logger = logging.getLogger("MarsOS")

class CropBiomonitor:
    def __init__(self):
        self.biomass_index = 50.0  # 0-100
        self.soil_moisture = 60.0
        self.health = 95.0

    def monitor_and_irrigate(self, os: MarsProductionOS):
        irrigation_cost = 1.2 if self.soil_moisture < 40 else 0.4
        os.power_battery = max(0.0, os.power_battery - irrigation_cost)

        self.soil_moisture = min(100.0, self.soil_moisture + 15)
        self.biomass_index = min(100.0, self.biomass_index + 2.5)
        self.health = max(60.0, self.health - 0.5 if os.ambient_temp < -50 else self.health)

        logger.info(f"[CROP] Biomass: {self.biomass_index:.1f} | Moisture: {self.soil_moisture:.1f}% | Health: {self.health:.1f}%")
