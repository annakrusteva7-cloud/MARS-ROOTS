pythonclass MarsIrrigationLogic:
    def __init__(self):
        self.water_inventory = 500  # liters
        self.power_level = 100      # battery percentage

    def should_i_water(self, soil_moisture, plant_stress_index):
        if self.power_level < 20:
            return "WAIT: Low power. Conserving energy for critical systems."

        if soil_moisture < 30:
            if plant_stress_index > 0.7:
                return self.execute_watering(amount=10) # Critical watering
            return self.execute_watering(amount=5)      # Optimal watering
        
        return "SKIP: Soil moisture adequate. Conserving water."

    def execute_watering(self, amount):
        self.water_inventory -= amount
        return f"ACTION: Dispensed {amount}L. Remaining Water: {self.water_inventory}L"

# Simulation execution
system = MarsIrrigationLogic()
print(system.should_i_water(soil_moisture=25, plant_stress_index=0.4))
