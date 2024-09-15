class Bonding:
    def __init__(self, level=1):
        """
        Initialize a Bonding instance with a default bonding level.
        """
        self.level = level

    def set_level(self, level):
        """
        Set the bonding level to the provided value and return a status message.
        
        Args:
            level (int): The bonding level to set, must be between 1 and 10.
        
        Returns:
            str: Confirmation message of the updated bonding level.
        """
        if 1 <= level <= 10:
            self.level = level
            return f"Bonding level set to: {self.level}/10"
        else:
            return "Error: Bonding level must be between 1 and 10."
