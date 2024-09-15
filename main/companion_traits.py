class CompanionTraits:
    def __init__(self):
        """
        Initialize the CompanionTraits class with an empty traits dictionary.
        """
        self.traits = {}

    def set_traits(self, name=None, age=None, gender=None, personality=None, likes=None, dislikes=None, tone=None, 
                   emotional_depth=None, abilities=None, primary_role=None, motivation=None, communication_style=None, 
                   quirks=None, emotional_triggers=None, humor_style=None, energy_level=None, confidence_level=None, 
                   worldview=None, ideal_relationship=None, learning_speed=None, emotional_sensitivity=None, 
                   curiosity_level=None, adaptability=None, moral_compass=None):
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
            humor_style (str): The companion's style of humor (e.g., sarcasm, dry, light, avoids humor).
            energy_level (str): The companion's energy level (e.g., enthusiastic, calm).
            confidence_level (str): The companion's confidence level (e.g., timid, assertive).
            worldview (str): The companion's general outlook (e.g., optimistic, cynical, pragmatic).
            ideal_relationship (str): The ideal relationship (e.g., supportive, mentor, playful friend, romantic).
            learning_speed (str): How quickly the companion learns (e.g., slow, average, fast).
            emotional_sensitivity (str): How attuned the companion is to emotions (e.g., low, moderate, high).
            curiosity_level (str): The companion's curiosity level (e.g., low, moderate, high).
            adaptability (str): The companion's ability to adapt (e.g., low, moderate, high).
            moral_compass (str): The companion's ethical stance (e.g., flexible, neutral, strict).
        
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
            "emotional_triggers": emotional_triggers,
            "humor_style": humor_style,
            "energy_level": energy_level,
            "confidence_level": confidence_level,
            "worldview": worldview,
            "ideal_relationship": ideal_relationship,
            "learning_speed": learning_speed,
            "emotional_sensitivity": emotional_sensitivity,
            "curiosity_level": curiosity_level,
            "adaptability": adaptability,
            "moral_compass": moral_compass
        })
        
        return f"Companion AI Traits set:\n\n{self.traits}"
