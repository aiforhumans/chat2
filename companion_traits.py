class CompanionTraits:
    def __init__(self):
        """
        Initialize the CompanionTraits class with an empty traits dictionary.
        """
        self.traits = {}

    def set_traits(self, name=None, age=None, gender=None, personality=None, likes=None, dislikes=None, tone=None, 
                   emotional_depth=None, abilities=None, primary_role=None, motivation=None, communication_style=None, 
                   quirks=None, emotional_triggers=None):
        """
        Set the traits of the companion. Any trait can be modified independently.
        
        Args:
            name (str): The companion's name.
            age (int): The companion's age.
            gender (str): The companion's gender.
            personality (str): The companion's personality description.
            likes (str): The companion's likes.
            dislikes (str): The companion's dislikes.
            tone (str): The companion's tone when interacting.
            emotional_depth (int): Emotional depth (e.g., how deeply the companion processes emotions).
            abilities (str): The companion's abilities.
            primary_role (str): The companion's primary role.
            motivation (str): What motivates the companion.
            communication_style (str): The communication style of the companion.
            quirks (str): Any quirks the companion has.
            emotional_triggers (str): Triggers that emotionally impact the companion.
        
        Returns:
            str: Confirmation message with updated traits.
        """
        self.traits.update({
            "name": name,
            "age": age,
            "gender": gender,
            "personality": personality,
            "likes": likes,
            "dislikes": dislikes,
            "tone": tone,
            "emotional_depth": emotional_depth,
            "abilities": abilities,
            "primary_role": primary_role,
            "motivation": motivation,
            "communication_style": communication_style,
            "quirks": quirks,
            "emotional_triggers": emotional_triggers
        })
        
        return f"Companion AI Traits set:\n\n{self.traits}"
