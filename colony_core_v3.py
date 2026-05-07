import random
import time
from datetime import datetime
import math

class MarsColonyEngineV3:
    """
    MARS-ROOTS v3.0.1: High-Fidelity Integrated Habitat OS.
    Features: Stefan-Boltzmann Thermal Physics, Predictive AI, 
    Earth-Mars Latency Simulation, and Critical Hibernation Protocols.
    """
    def __init__(self, commander_name):
        self.commander = commander_name
        self.version = "3.0.1-STABLE"
        self.power_grid = 100.0
        self.water_reserve = 1000.0
        self.power_history = [100.0, 98.5, 97.2, 95.8] # Data for AI analysis
        
        # Physics & Environment Constants
        self.mars_surface_temp = -65.0      # Average Martian Temp (Celsius)
        self.stefan_boltzmann_const = 5.67e-8
        self.earth_distance_light_min = 20   # Communication lag in minutes
        
        # System Health & Redundancy
        self.primary_node_active = True
        self.hibernation_mode = False

    def log_event(self, message):
        """Internal logging for mission records."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")

    def thermal_physics_module(self):
        """Calculates heat flux loss using Stefan-Boltzmann Law."""
        # Convert Celsius to Kelvin
        temp_k = self.mars_surface_temp + 273.15
        # Calculate Power radiated per unit area (P = e * sigma * T^4)
        heat_loss = self.stefan_boltzmann_const * (temp_k**4)
        efficiency_impact = (heat_loss / 100) * 0.4
        self.power_grid -= efficiency_impact
        self.log_event(f"PHYSICS: Heat Flux Loss: {heat_loss:.2f} W/m2. Impact: -{efficiency_impact:.2f}%")

    def integrated_irrigation_system(self, soil_moisture, plant_stress):
        """Integrated Life-Support: Smart Irrigation logic."""
        if self.hibernation_mode:
            return # Skip if in energy saving mode
            
        temp_factor = 1.2 if self.mars_surface_temp > -20 else 1.0
        if soil_moisture < 30:
            amount = 10 * temp_factor if plant_stress > 0.7 else 5 * temp_factor
            self.water_reserve -= amount
            self.log_event(f"ACTION: Dispensed {amount:.1f}L water. Reservoir: {self.water_reserve:.1f}L")

    def predictive_ai_analysis(self):
        """Simulated Predictive AI: Trend analysis for energy depletion."""
        if len(self.power_history) > 3:
            # Simple Linear Trend Analysis
            avg_drain = (self.power_history[0] - self.power_history[-1]) / len(self.power_history)
            cycles_left = self.power_grid / avg_drain if avg_drain > 0 else 999
            self.log_event(f"AI-PREDICT: Energy depletion ETA: {cycles_left:.1f} cycles.")
            
            if cycles_left < 10:
                self.log_event("WARNING: Critically low energy trend detected!")

    def send_telemetry_to_earth(self):
        """Simulates the physics of Earth-Mars communication latency."""
        self.log_event(f"COMMS: Telemetry packet sent. Signal lag: {self.earth_distance_light_min} min.")

    def check_hibernation_protocol(self):
        """Safety protocol to prevent total base blackout."""
        if self.power_grid < 10.0:
            self.hibernation_mode = True
            self.log_event("CRITICAL: Entering HIBERNATION MODE. All non-essential systems OFF.")
            return True
        return False

    def run_cycle(self):
        print(f"\n>>> MARS-ROOTS v{self.version} Operational Cycle Starting...")
        
        if self.check_hibernation_protocol():
            print(">>> SYSTEM STATUS: HIBERNATED (Oxygen Generation ONLY)")
            return

        self.thermal_physics_module()
        self.predictive_ai_analysis()
        self.integrated_irrigation_system(random.uniform(20, 40), random.uniform(0.1, 0.9))
        self.send_telemetry_to_earth()
        
        # Energy consumption
        drain = random.uniform(0.5, 1.5)
        self.power_grid -= drain
        self.power_history.append(self.power_grid)
        
        print(f"--- CYCLE COMPLETE | Power: {self.power_grid:.1f}% | Water: {self.water_reserve:.1f}L ---")

if __name__ == "__main__":
    # Start the mission
    engine = MarsColonyEngineV3(commander_name="Ivanov")
    
    # Run simulation for 3 cycles
    for _ in range(3):
        engine.run_cycle()
        time.sleep(1) # Visual delay for the simulation
