import pyttsx3

class MarsVoiceAssistant:
    """Handles crew vocal communication and alerts."""
    def __init__(self):
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 150)
            self.active = True
        except:
            self.active = False

    def announce(self, message):
        print(f"[AI VOICE]: \"{message}\"")
        if self.active:
            try:
                self.engine.say(message)
                self.engine.runAndWait()
            except:
                pass

if __name__ == "__main__":
    ai = MarsVoiceAssistant()
    ai.announce("Vocal systems online. Welcome to MARS-ROOTS v4.0.")
