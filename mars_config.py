import json
from dataclasses import dataclass, asdict
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger("MarsOS")

@dataclass
class MarsConfig:
    seed: int = 42
    total_sols: int = 10
    battery_capacity: float = 100.0
    max_dust_threshold: float = 25.0
    heater_factor: float = 0.02
    arm_power_cost: float = 8.5
    background_drain: float = 2.5

    def save(self, path: str = "mars_state.json"):
        try:
            with open(path, "w") as f:
                json.dump(asdict(self), f, indent=2)
            logger.info(f"Telemetry persisted to {path}")
        except Exception as e:
            logger.error(f"Persistence failed: {e}")

    @classmethod
    def load(cls, path: str = "mars_state.json"):
        try:
            if Path(path).exists():
                with open(path) as f:
                    data = json.load(f)
                return cls(**data)
        except Exception:
            pass
        return cls()
