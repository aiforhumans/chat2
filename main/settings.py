import json
from companion_traits import CompanionTraits
from user_info import UserInfo
from scenario import Scenario
from bonding import Bonding

class Settings:
    def __init__(self, companion_traits: CompanionTraits, user_info: UserInfo, scenario: Scenario, bonding: Bonding):
        """
        Initialize Settings with companion traits, user info, scenario, and bonding.
        """
        self.companion_traits = companion_traits
        self.user_info = user_info
        self.scenario = scenario
        self.bonding = bonding

    def save(self):
        """
        Save the current settings to a JSON file.
        
        Returns:
            str: Status message indicating success or failure.
        """
        settings = {
            "companion_traits": self.companion_traits.traits,
            "user_info": self.user_info.info,
            "scenario": self.scenario.scenario,
            "bonding_level": self.bonding.level
        }
        try:
            with open("companion_settings.json", "w") as f:
                json.dump(settings, f)
            return "Settings saved successfully!"
        except Exception as e:
            return f"Error saving settings: {e}"

    def load(self):
        """
        Load settings from a JSON file and apply them.
        
        Returns:
            str: Status message with loaded settings or an error if not found.
        """
        try:
            with open("companion_settings.json", "r") as f:
                settings = json.load(f)
            self.companion_traits.traits = settings["companion_traits"]
            self.user_info.info = settings["user_info"]
            self.scenario.scenario = settings["scenario"]
            self.bonding.level = settings["bonding_level"]
            return (f"Settings loaded successfully!\n\nCompanion Traits:\n{self.companion_traits.traits}\n\n"
                    f"User Info:\n{self.user_info.info}\n\nScenario:\n{self.scenario.scenario}\n\n"
                    f"Bonding Level: {self.bonding.level}/10")
        except FileNotFoundError:
            return "No saved settings found."
        except Exception as e:
            return f"Error loading settings: {e}"
