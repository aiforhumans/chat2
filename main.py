import gradio as gr
from companion_traits import CompanionTraits
from user_info import UserInfo
from scenario import Scenario
from bonding import Bonding
from settings import Settings
from chat import Chat

def create_chat_interface(chat):
    """
    Create the chat interface for interacting with the AI companion.
    """
    return gr.ChatInterface(
        fn=chat.chatbot,
        chatbot=gr.Chatbot(height=600),
        title="Companion AI Roleplay",
        description="Interact with your personalized AI companion in a rich roleplay scenario.",
        examples=[["Tell me about yourself"], ["What's our current adventure?"]],
        theme="soft"
    )

def create_companion_traits_interface(companion_traits):
    """
    Create the companion traits setting interface with descriptions for each input.
    """
    return gr.Interface(
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
            gr.Textbox(label="Emotional Triggers", lines=3),
            gr.Dropdown(["Sarcasm", "Dry", "Light", "Avoids Humor"], label="Humor Style"),
            gr.Dropdown(["Enthusiastic", "Balanced", "Calm"], label="Energy Level"),
            gr.Dropdown(["Timid", "Moderate", "Assertive"], label="Confidence Level"),
            gr.Dropdown(["Optimistic", "Pragmatic", "Cynical"], label="Worldview"),
            gr.Dropdown(["Supportive", "Mentor", "Playful Friend", "Romantic"], label="Ideal Companion Relationship"),
            gr.Dropdown(["Slow", "Average", "Fast"], label="Learning Speed"),
            gr.Dropdown(["Low", "Moderate", "High"], label="Emotional Sensitivity"),
            gr.Dropdown(["Low", "Moderate", "High"], label="Curiosity Level"),
            gr.Dropdown(["Low", "Moderate", "High"], label="Adaptability"),
            gr.Dropdown(["Flexible", "Neutral", "Strict"], label="Moral Compass")
        ],
        outputs="text",
        title="Companion AI Traits",
        description="""
        Please fill out the traits for your AI companion. Explanations are provided above each input field.
        """,
        allow_flagging="never"
    )




def create_user_info_interface(user_info):
    """
    Create the user information setting interface.
    """
    return gr.Interface(
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

def create_scenario_interface(scenario):
    """
    Create the scenario setting interface.
    """
    return gr.Interface(
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

def create_bonding_interface(bonding):
    """
    Create the bonding level setting interface.
    """
    return gr.Interface(
        fn=bonding.set_level,
        inputs=[gr.Slider(1, 10, label="Bonding Level")],
        outputs="text",
        title="Emotional Bonding",
        description="Set the current level of connection between you and your AI companion.",
        allow_flagging="never"
    )

def create_settings_interface(settings):
    """
    Create the settings interface for saving and loading settings.
    """
    return gr.Interface(
        fn=lambda action: settings.save() if action == "save" else settings.load(),
        inputs=gr.Radio(["save", "load"], label="Action"),
        outputs="text",
        title="Settings",
        description="Save or load your companion AI settings.",
        allow_flagging="never"
    )

def create_interfaces(chat, companion_traits, user_info, scenario, bonding, settings):
    """
    Create the tabbed interface by integrating all the individual interfaces.
    """
    return gr.TabbedInterface(
        [
            create_chat_interface(chat),
            create_companion_traits_interface(companion_traits),
            create_user_info_interface(user_info),
            create_scenario_interface(scenario),
            create_bonding_interface(bonding),
            create_settings_interface(settings)
        ],
        ["Chat", "Companion Traits", "User Info", "Scenario", "Bonding", "Settings"]
    )

if __name__ == "__main__":
    companion_traits = CompanionTraits()
    user_info = UserInfo()
    scenario = Scenario()
    bonding = Bonding()
    settings = Settings(companion_traits, user_info, scenario, bonding)
    chat = Chat(companion_traits, user_info, scenario, bonding)

    demo = create_interfaces(chat, companion_traits, user_info, scenario, bonding, settings)
    demo.launch()
