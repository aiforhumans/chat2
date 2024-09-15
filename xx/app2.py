import gradio as gr
from openai import OpenAI
import json

# API constants
OPENAI_BASE_URL = "http://localhost:1234/v1"
OPENAI_API_KEY = "lm-studio"

class CompanionTraits:
    def __init__(self):
        self.traits = {}

    def set_traits(self, name, age, gender, personality, likes, dislikes, tone, emotional_depth, abilities, 
                   primary_role, motivation, communication_style, quirks, emotional_triggers):
        self.traits = {
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
        }
        return f"Companion AI Traits set:\n\n{self.traits}"

class UserInfo:
    def __init__(self):
        self.info = {}

    def set_info(self, name, age, relationship, preferences):
        self.info = {
            "name": name,
            "age": age,
            "relationship": relationship,
            "preferences": preferences
        }
        return f"User Info set:\n\n{self.info}"

class Scenario:
    def __init__(self):
        self.scenario = {}

    def set_scenario(self, setting, time_period, objective, events, rules, role):
        self.scenario = {
            "setting": setting,
            "time_period": time_period,
            "objective": objective,
            "events": events,
            "rules": rules,
            "role": role
        }
        return f"Scenario set:\n\n{self.scenario}"

class Bonding:
    def __init__(self):
        self.level = 1

    def set_level(self, level):
        self.level = level
        return f"Bonding level set to: {self.level}/10"

class Settings:
    def __init__(self, companion_traits, user_info, scenario, bonding):
        self.companion_traits = companion_traits
        self.user_info = user_info
        self.scenario = scenario
        self.bonding = bonding

    def save(self):
        settings = {
            "companion_traits": self.companion_traits.traits,
            "user_info": self.user_info.info,
            "scenario": self.scenario.scenario,
            "bonding_level": self.bonding.level
        }
        with open("companion_settings.json", "w") as f:
            json.dump(settings, f)
        return "Settings saved successfully!"

    def load(self):
        try:
            with open("companion_settings.json", "r") as f:
                settings = json.load(f)
            self.companion_traits.traits = settings["companion_traits"]
            self.user_info.info = settings["user_info"]
            self.scenario.scenario = settings["scenario"]
            self.bonding.level = settings["bonding_level"]
            return f"Settings loaded successfully!\n\nCompanion Traits:\n{self.companion_traits.traits}\n\nUser Info:\n{self.user_info.info}\n\nScenario:\n{self.scenario.scenario}\n\nBonding Level: {self.bonding.level}/10"
        except FileNotFoundError:
            return "No saved settings found."

class Chat:
    def __init__(self, companion_traits, user_info, scenario, bonding):
        self.companion_traits = companion_traits
        self.user_info = user_info
        self.scenario = scenario
        self.bonding = bonding
        self.openai_client = OpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)

    def get_completion(self, model_name, messages):
        completion = self.openai_client.chat.completions.create(
            model=model_name,
            messages=messages
        )
        return completion.choices[0].message.content

    def chatbot(self, message, history):
        system_message = f"""
        You are a companion AI with the following traits:
        {self.companion_traits.traits}
        
        You are interacting with a user who has the following profile:
        {self.user_info.info}
        
        The current roleplay scenario is:
        {self.scenario.scenario}
        
        The current bonding level between you and the user is: {self.bonding.level}/10
        
        Adjust your responses according to your traits, the user's info, the given scenario, and the bonding level. 
        Maintain your character and role throughout the interaction.
        """
        
        messages = [{"role": "system", "content": system_message}]
        
        for human, assistant in history:
            messages.append({"role": "user", "content": human})
            messages.append({"role": "assistant", "content": assistant})
        
        messages.append({"role": "user", "content": message})
        
        response = self.get_completion("gpt-4o", messages)
        return response

def create_interfaces(chat, companion_traits, user_info, scenario, bonding, settings):
    chat_iface = gr.ChatInterface(
        fn=chat.chatbot,
        chatbot=gr.Chatbot(height=600),
        title="Companion AI Roleplay",
        description="Interact with your personalized AI companion in a rich roleplay scenario.",
        examples=[["Tell me about yourself"], ["What's our current adventure?"]],
        theme="soft"
    )

    companion_traits_iface = gr.Interface(
        fn=companion_traits.set_traits,
        inputs=[
            gr.Textbox(label="Name"),
            gr.Number(label="Age"),
            gr.Dropdown(["Male", "Female", "Non-binary", "Other"], label="Gender"),
            gr.Textbox(label="Personality", lines=3),
            gr.Textbox(label="Likes", lines=3),
            gr.Textbox(label="Dislikes", lines=3),
            gr.Dropdown(["Warm and friendly", "Professional", "Playful", "Affectionate"], label="Tone of Communication"),
            gr.Slider(1, 10, label="Emotional Depth"),
            gr.Textbox(label="Special Abilities/Skills", lines=3),
            gr.Dropdown(["Emotional support", "Problem-solver", "Adventurer", "Listener", "Motivator"], label="Primary Role"),
            gr.Textbox(label="Motivation", lines=3),
            gr.Dropdown(["Direct", "Suggestive", "Secretive", "Enthusiastic"], label="Communication Style"),
            gr.Textbox(label="Quirks", lines=3),
            gr.Textbox(label="Emotional Triggers", lines=3)
        ],
        outputs="text",
        title="Companion AI Traits",
        description="Set the traits for your AI companion.",
        allow_flagging="never"
    )

    user_info_iface = gr.Interface(
        fn=user_info.set_info,
        inputs=[
            gr.Textbox(label="Name of User"),
            gr.Number(label="User Age"),
            gr.Dropdown(["Best friend", "Guardian", "Partner", "Confidant", "Pet"], label="Relationship with AI"),
            gr.Textbox(label="User's Preferences in AI", lines=3)
        ],
        outputs="text",
        title="User Info",
        description="Set your information for the roleplay.",
        allow_flagging="never"
    )

    scenario_iface = gr.Interface(
        fn=scenario.set_scenario,
        inputs=[
            gr.Textbox(label="Setting", lines=3),
            gr.Dropdown(["Present day", "Medieval Fantasy", "Futuristic Sci-fi", "Post-apocalyptic"], label="Time Period"),
            gr.Textbox(label="Main Objective or Theme", lines=3),
            gr.Textbox(label="Key Events or Milestones", lines=3),
            gr.Textbox(label="Special Rules/Boundaries", lines=3),
            gr.Dropdown(["Emotional support", "Problem-solver", "Adventurer", "Listener", "Motivator"], label="Companion's Role")
        ],
        outputs="text",
        title="Roleplay Scenario",
        description="Set the scenario for your roleplay experience.",
        allow_flagging="never"
    )

    bonding_iface = gr.Interface(
        fn=bonding.set_level,
        inputs=[
            gr.Slider(1, 10, label="Bonding Level")
        ],
        outputs="text",
        title="Emotional Bonding",
        description="Set the current level of connection between you and your AI companion.",
        allow_flagging="never"
    )

    settings_iface = gr.Interface(
        fn=lambda action: settings.save() if action == "save" else settings.load(),
        inputs=gr.Radio(["save", "load"], label="Action"),
        outputs="text",
        title="Settings",
        description="Save or load your companion AI settings.",
        allow_flagging="never"
    )

    return gr.TabbedInterface([chat_iface, companion_traits_iface, user_info_iface, scenario_iface, bonding_iface, settings_iface], 
                              ["Chat", "Companion Traits", "User Info", "Scenario", "Bonding", "Settings"])

if __name__ == "__main__":
    companion_traits = CompanionTraits()
    user_info = UserInfo()
    scenario = Scenario()
    bonding = Bonding()
    settings = Settings(companion_traits, user_info, scenario, bonding)
    chat = Chat(companion_traits, user_info, scenario, bonding)
    
    demo = create_interfaces(chat, companion_traits, user_info, scenario, bonding, settings)
    demo.launch()
