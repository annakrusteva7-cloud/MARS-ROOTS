import time
import random
from datetime import datetime

class MarsRootsMasterOS:
    """
    Core Operating System for managing a Martian habitat.
    Handles resources, autonomous drones, and survival protocols.
    """
    def __init__(self, astronaut_name):
        self.user = astronaut_name
        self.log_file = "mission_log.txt"
        self.power = 100.0
        self.water = 100.0
        self.oxygen = 21.0
        self.resources = []
        
        self.log_event("--- Master OS Initialized ---")
        self.speak(f"Systems online. Welcome to MARS-ROOTS, Commander {self.user}.")

    def log_event(self, message):
        """Records critical mission events to a local text file."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")

    def speak(self, text):
        """Simulates AI voice feedback for the crew."""
        print(f"\n[AI VOICE]: \"{text}\"")

    def display_dashboard(self):
        """Visualizes base statistics and resource levels in the console."""
        print("\n" + "="*55)
        print(f" MARS-ROOTS DASHBOARD | UTC: {datetime.now().strftime('%H:%M')}")
        print("="*55)
        print(f" POWER: {self.power:.1f}% | WATER: {self.water:.1f}% | O2: {self.oxygen:.1f}%")
        print(f" SYSTEM STATUS: {'[OPTIMAL]' if self.power > 40 else '[LOW POWER MODE]'}")
        print(f" DISCOVERED RESOURCES: {', '.join(self.resources) if self.resources else 'None'}")
        print("="*55)

    def environment_simulation(self):
        """Simulates dynamic changes in the harsh Martian environment."""
        self.power -= random.uniform(0.5, 2.0)
        self.water -= random.uniform(0.1, 1.0)
        
        if random.random() < 0.2:
            self.speak("Warning: Dust storm detected. Solar efficiency decreasing!")
            self.power -= 5.0
            self.log_event("METEO: Dust storm event recorded.")

    def run_scout_drone(self):
        """Launches an autonomous drone to scout for raw materials nearby."""
        if self.power < 30:
            self.speak("Energy too low for drone deployment. Mission aborted.")
            return

        self.speak("ARES Scout Drone is launching for reconnaissance...")
        time.sleep(1) 
        
        findings = ["Water Ice", "Minerals", "Iron Ore", None]
        found = random.choice(findings)
        
        if found:
            self.resources.append(found)
            self.speak(f"Success! Drone discovered {found}. Recording coordinates.")
            self.log_event(f"DRONE: Resource discovered - {found}")
        else:
            self.speak("Reconnaissance complete. No new resources detected.")

    def emergency_protocol(self):
        """Self-preservation logic when energy levels are critical."""
        if self.power < 20:
            self.speak("CRITICAL: Switching to emergency power. Shading non-essential modules.")
            self.log_event("SYSTEM: Emergency power protocol activated.")

    def main_loop(self):
        """The main operational loop of the Mars Roots mission."""
        try:
            for cycle in range(1, 4): 
                print(f"\n>>> Mission Cycle {cycle} starting...")
                self.environment_simulation()
                self.emergency_protocol()
                self.display_dashboard()
                
                if cycle == 2:
                    self.run_scout_drone()
                
                time.sleep(2) 
            
            self.speak("All scheduled tasks completed. Awaiting further commands.")
        except KeyboardInterrupt:
            self.speak("Safe shutdown sequence initiated by user.")

if __name__ == "__main__":
    my_base = MarsRootsMasterOS("Ivanov")
    my_base.main_loop()
