from openai import OpenAI

# Constants
BASE_URL = "http://localhost:1234/v1"
API_KEY = "lm-studio"

# Initialize client
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

# Define traits
traits = [
    "name",
    "age",
    "gender",
    "personality",
    "likes",
    "dislikes",
    "tone",
    "emotional_depth",
    "abilities",
    "primary_role",
    "motivation",
    "communication_style",
    "quirks",
    "emotional_triggers",
]

# Generate completion
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a roleplay expert "},
        {"role": "user", "content": f"create for a companion AI the following traits:{', '.join(traits)}"},
    ]
)

print(completion.choices[0].message.content)
