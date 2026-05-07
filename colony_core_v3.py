import random
import time
from datetime import datetime
import math

class MarsColonyEngineV3:
    """
    MARS-ROOTS v3.0: Integrated Habitat OS.
    Features: Predictive AI, Stefan-Boltzmann Thermal Dynamics, 
    and Integrated Precision Irrigation.
    """
    def __init__(self, commander_name):
        self.commander = commander_name
        self.version = "3.0.0-INTEGRATED"
        self.power_grid = 100.0
        self.water_reserve = 1000.0
        self.power_history = [100.0, 98.2, 97.5, 96.1]
        
        # Physics & Environment
        self.mars_surface_temp = -65.0      
        self.stefan_boltzmann_const = 5.67e-8
        
        # Redundancy System
        self.primary_node_active = True

    def thermal_physics_module(self):
        """Calculates heat flux loss using Stefan-Boltzmann Law."""
        temp_k = self.mars_surface_temp + 273.15
        heat_loss = self.stefan_boltzmann_const * (temp_k**4)
        efficiency_impact = (heat_loss / 100) * 0.4
        self.power_grid -= efficiency_impact
        print(f"[PHYSICS]: Heat Flux Loss: {heat_loss:.2f} W/m2. Power impact: -{efficiency_impact:.2f}%")

    def integrated_irrigation_system(self, soil_moisture, plant_stress):
        """
        Sub-module: Advanced Irrigation Logic.
        Integrated directly into the Core Engine.
        """
        print(f"[IRRIGATION]: Checking sensors... Moisture: {soil_moisture}%")
        
        # Temperature-aware watering
        temp_factor = 1.2 if self.mars_surface_temp > -20 else 1.0
        
        if soil_moisture < 30:
            amount = 10 * temp_factor if plant_stress > 0.7 else 5 * temp_factor
            self.water_reserve -= amount
            print(f"[ACTION]: Dispensed {amount:.1f}L of water. Reservoir: {self.water_reserve:.1f}L")
        else:
            print("[STATUS]: Soil moisture optimal. Skipping watering cycle.")

    def predictive_ai_analysis(self):
        """Predicts resource depletion trends."""
        if len(self.power_history) > 3:
            avg_drain = (self.power_history[0] - self.power_history[-1]) / len(self.power_history)
            cycles_left = self.power_grid / avg_drain if avg_drain > 0 else 999
            print(f"[AI-PREDICT]: Energy depletion ETA: {cycles_left:.1f} cycles.")

    def run_cycle(self):
        print(f"\n>>> MARS-ROOTS v{self.version} Cycle starting...")
        self.thermal_physics_module()
        self.predictive_ai_analysis()
        
        # Simulating random sensor data for irrigation
        current_moisture = random.uniform(20, 40)
        current_stress = random.uniform(0.1, 0.9)
        self.integrated_irrigation_system(current_moisture, current_stress)
        
        # Resource drain
        self.power_grid -= random.uniform(0.3, 0.8)
        self.power_history.append(self.power_grid)
        print(f"STATUS: Power: {self.power_grid:.1f}% | Water: {self.water_reserve:.1f}L")

if __name__ == "__main__":
    engine = MarsColonyEngineV3("Ivanov")
    for _ in range(3):
        engine.run_cycle()
        time.sleep(1)
