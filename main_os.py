import time

class MarsGreenhouseOS:
    def __init__(self):
        self.earth_connection = False  # Simulating lost connection to Earth
        self.radiation_level = 0.5     # Nominal level

    def monitor_conditions(self):
        if self.radiation_level > 0.8:
            return "DANGER: Solar Flare Detected"
        return "NORMAL"

    def autonomous_decision(self, status):
        if not self.earth_connection:
            print("--- Running on Local Edge AI (No Earth Link) ---")
            if status == "DANGER: Solar Flare Detected":
                self.activate_protective_mode()
            else:
                print("Status: Nominal. Continuing autonomous operations.")

    def activate_protective_mode(self):
        print("ACTION: Closing radiation shields and redirecting power to life support.")

# Simulation execution
os = MarsGreenhouseOS()
os.autonomous_decision(os.monitor_conditions())
