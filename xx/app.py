import gradio as gr
from openai import OpenAI
import json

# API constants
OPENAI_BASE_URL = "http://localhost:1234/v1"
OPENAI_API_KEY = "lm-studio"

# API setup
openai_client = OpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)

# Global variables to store companion AI traits, user info, scenario, and bonding level
companion_traits = {}
user_info = {}
scenario = {}
bonding_level = 1

def get_completion(model_name, messages):
    completion = openai_client.chat.completions.create(
        model=model_name,
        messages=messages
    )
    return completion.choices[0].message.content

def chatbot(message, history):
    global companion_traits, user_info, scenario, bonding_level
    
    companion_traits_str = "\n".join([f"{k}: {v}" for k, v in companion_traits.items()])
    user_info_str = "\n".join([f"{k}: {v}" for k, v in user_info.items()])
    scenario_str = "\n".join([f"{k}: {v}" for k, v in scenario.items()])
    
    system_message = f"""You are a companion AI with the following traits:
{companion_traits_str}

You are interacting with a user who has the following profile:
{user_info_str}

The current roleplay scenario is:
{scenario_str}

The current bonding level between you and the user is: {bonding_level}/10

Adjust your responses according to your traits, the user's info, the given scenario, and the bonding level. 
Maintain your character and role throughout the interaction."""

    messages = [{"role": "system", "content": system_message}]
    
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    
    messages.append({"role": "user", "content": message})
    
    response = get_completion("gpt-4o", messages)
    return response

def set_companion_traits(name, age, gender, personality, likes, dislikes, tone, emotional_depth, abilities, 
                         primary_role, motivation, communication_style, quirks, emotional_triggers):
    global companion_traits
    companion_traits = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Personality": personality,
        "Likes": likes,
        "Dislikes": dislikes,
        "Tone of Communication": tone,
        "Emotional Depth": emotional_depth,
        "Special Abilities/Skills": abilities,
        "Primary Role": primary_role,
        "Motivation": motivation,
        "Communication Style": communication_style,
        "Quirks": quirks,
        "Emotional Triggers": emotional_triggers
    }
    return f"Companion AI Traits set:\n\n{companion_traits}"

def set_user_info(name, age, relationship, preferences):
    global user_info
    user_info = {
        "Name": name,
        "Age": age,
        "Relationship with AI": relationship,
        "Preferences in AI": preferences
    }
    return f"User Info set:\n\n{user_info}"

def set_scenario(setting, time_period, objective, events, rules, role):
    global scenario
    scenario = {
        "Setting": setting,
        "Time Period": time_period,
        "Main Objective or Theme": objective,
        "Key Events or Milestones": events,
        "Special Rules/Boundaries": rules,
        "Companion's Role": role
    }
    return f"Scenario set:\n\n{scenario}"

def set_bonding_level(level):
    global bonding_level
    bonding_level = level
    return f"Bonding level set to: {bonding_level}/10"

def save_settings():
    global companion_traits, user_info, scenario, bonding_level
    settings = {
        "companion_traits": companion_traits,
        "user_info": user_info,
        "scenario": scenario,
        "bonding_level": bonding_level
    }
    with open("companion_settings.json", "w") as f:
        json.dump(settings, f)
    return "Settings saved successfully!"

def load_settings():
    global companion_traits, user_info, scenario, bonding_level
    try:
        with open("companion_settings.json", "r") as f:
            settings = json.load(f)
        companion_traits = settings["companion_traits"]
        user_info = settings["user_info"]
        scenario = settings["scenario"]
        bonding_level = settings["bonding_level"]
        return f"Settings loaded successfully!\n\nCompanion Traits:\n{companion_traits}\n\nUser Info:\n{user_info}\n\nScenario:\n{scenario}\n\nBonding Level: {bonding_level}/10"
    except FileNotFoundError:
        return "No saved settings found."

chat_iface = gr.ChatInterface(
    fn=chatbot,
    chatbot=gr.Chatbot(height=600),
    title="Companion AI Roleplay",
    description="Interact with your personalized AI companion in a rich roleplay scenario.",
    examples=[["Tell me about yourself"], ["What's our current adventure?"]],
    theme="soft"
)

companion_traits_iface = gr.Interface(
    fn=set_companion_traits,
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
    fn=set_user_info,
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
    fn=set_scenario,
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
    fn=set_bonding_level,
    inputs=[
        gr.Slider(1, 10, label="Bonding Level")
    ],
    outputs="text",
    title="Emotional Bonding",
    description="Set the current level of connection between you and your AI companion.",
    allow_flagging="never"
)

settings_iface = gr.Interface(
    fn=lambda action: save_settings() if action == "save" else load_settings(),
    inputs=gr.Radio(["save", "load"], label="Action"),
    outputs="text",
    title="Settings",
    description="Save or load your companion AI settings.",
    allow_flagging="never"
)

demo = gr.TabbedInterface([chat_iface, companion_traits_iface, user_info_iface, scenario_iface, bonding_iface, settings_iface], 
                          ["Chat", "Companion Traits", "User Info", "Scenario", "Bonding", "Settings"])

if __name__ == "__main__":
    demo.launch()
