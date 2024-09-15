class Scenario:
    def __init__(self):
        """
        Initialize the Scenario class with an empty scenario dictionary.
        """
        self.scenario = {}

    def set_scenario(self, setting=None, time_period=None, objective=None, events=None, rules=None, role=None):
        """
        Set or update the scenario details. Each field is optional and can be updated individually.
        
        Args:
            setting (str): The setting of the scenario.
            time_period (str): The time period for the scenario.
            objective (str): The main objective of the scenario.
            events (str): Key events that take place in the scenario.
            rules (str): Any rules or guidelines for the scenario.
            role (str): The role that the companion or user plays in the scenario.
        
        Returns:
            str: Confirmation message with the updated scenario details.
        """
        self.scenario.update({
            "setting": setting,
            "time_period": time_period,
            "objective": objective,
            "events": events,
            "rules": rules,
            "role": role
        })
        
        return f"Scenario set:\n\n{self.scenario}"
