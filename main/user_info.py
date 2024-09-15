class UserInfo:
    def __init__(self):
        """
        Initialize the UserInfo class with an empty info dictionary.
        """
        self.info = {}

    def set_info(self, name=None, age=None, relationship=None, preferences=None):
        """
        Set or update user information for the roleplay.
        
        Args:
            name (str): Name of the user.
            age (int): Age of the user.
            relationship (str): Relationship between the user and the AI.
            preferences (str): User's preferences in interacting with the AI.
        
        Returns:
            str: A confirmation message with the updated user info.
        """
        self.info.update({
            "name": name,
            "age": age,
            "relationship": relationship,
            "preferences": preferences
        })
        return f"User Info set:\n\n{self.info}"
