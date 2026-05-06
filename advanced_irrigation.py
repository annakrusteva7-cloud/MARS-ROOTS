import time
from datetime import datetime
import random

class MarsIrrigationLogic:
    """
    Advanced Irrigation Management for Martian Habitats.
    Adjusts water flow based on moisture, plant stress, and ambient temperature.
    """
    def __init__(self):
        self.water_inventory = 500  # Liters
        self.power_level = 100      # Battery %
        self.log_file = "mission_log.txt"
        self.optimal_temp = 22.0    # Celsius

    def log_action(self, message):
        """Records actions to the mission log."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] IRRIGATION: {message}\n")

    def analyze_irrigation_need(self, soil_moisture, plant_stress_index, temperature):
        """
        Decision-making logic considering evaporation rates and plant health.
        """
        print(f"\n[SENSOR DATA]: Moisture: {soil_moisture}% | Stress: {plant_stress_index} | Temp: {temperature}°C")

        # Emergency Power Check
        if self.power_level < 20:
            return "WAIT: Low power. Postponing irrigation."

        # Water Supply Check
        if self.water_inventory <= 0:
            return "CRITICAL: Out of water!"

        # Temperature-based Multiplier (Simulating Evaporation)
        # If temp > 30°C, we increase water amount by 20%
        temp_multiplier = 1.2 if temperature > 30 else 1.0

        if soil_moisture < 30:
            base_amount = 10 if plant_stress_index > 0.7 else 5
            final_amount = base_amount * temp_multiplier
            
            reason = "High Stress" if plant_stress_index > 0.7 else "Standard Need"
            if temp_multiplier > 1.0:
                reason += " + High Temp Compensation"
                
            return self.execute_watering(final_amount, reason)
        
        return "SKIP: Soil moisture adequate."

    def execute_watering(self, amount, reason):
        """Processes the watering action."""
        if self.water_inventory < amount:
            amount = self.water_inventory
        
        self.water_inventory -= amount
        result = f"ACTION: Dispensed {amount:.1f}L ({reason}). Remaining: {self.water_inventory:.1f}L"
        print(f"[SYSTEM]: {result}")
        self.log_action(result)
        return result

# --- Simulation ---
if __name__ == "__main__":
    system = MarsIrrigationLogic()
    
    # Scenario: Hot day on Mars (35°C), low moisture
    system.analyze_irrigation_need(soil_moisture=20, plant_stress_index=0.5, temperature=35.0)
    
    # Scenario: Perfect conditions (22°C), but high plant stress
    system.analyze_irrigation_need(soil_moisture=25, plant_stress_index=0.9, temperature=22.0)
