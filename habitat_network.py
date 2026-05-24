import logging
from core_os import MarsProductionOS

logger = logging.getLogger("MarsOS")

class HabitatNetwork:
    def __init__(self, num_habitats=3):
        self.habitats = [MarsProductionOS() for _ in range(num_habitats)]

    def share_resources(self):
        total_battery = sum(h.power_battery for h in self.habitats)
        avg_battery = total_battery / len(self.habitats)
        for hab in self.habitats:
            hab.power_battery = round((hab.power_battery + avg_battery) / 2, 2)
        logger.info(f"Resource sharing complete. Network avg battery: {avg_battery:.1f}%")
