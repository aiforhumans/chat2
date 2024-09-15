
# AI Companion Project

## Overview
This project is an **AI Companion** that utilizes **LM Studio**, a **local LLM (Large Language Model)**, and **Gradio** for a user-friendly interface. The system is designed to create personalized conversations or roleplay settings with dynamic user inputs, such as personality traits and user data, while processing responses via a local LLM API server.

## Features
- **Local LLM** integration for enhanced privacy and performance.
- **Gradio**-powered web interface for seamless user interaction.
- Roleplay scenarios with customizable AI personalities and user settings.
- Multiple input fields for user-specific traits such as age, gender, and personality traits.
- Easy API handling to connect with local LLM (via LM Studio).

## Tech Stack
- **LM Studio**: Local LLM server used for processing AI responses.
- **Gradio**: Web-based interface for AI interaction and roleplay settings.
- **Python**: Main language used to handle the logic and communication between components.
  
## Components
The project is split into several modules for better code management and scalability:
- **api_debugger.py**: A utility for debugging API requests to the local LLM server.
- **bonding.py**: Handles the bonding or interaction logic between the AI companion and the user.
- **chat.py**: Manages the chat functionality between the user and the AI.
- **companion_traits.py**: Stores and manages AI personality traits for more dynamic interactions.
- **companion_settings.json**: Stores configuration settings for the AI companion's behavior and personality.
- **scenario.py**: Creates and configures roleplay scenarios.
- **settings.py**: Manages the configuration and settings of the AI and user experience.
- **user_info.py**: Manages user-specific information, such as age, gender, and traits.
- **create.py**: Possibly handles dynamic creation of new scenarios or AI personalities.
- **main.py**: The main entry point of the application that ties together the various components.
- **new.txt**: (Unclear purpose, possibly for storing some temporary or test data).

## Getting Started

### Prerequisites
- **Python 3.8+** (Make sure Python is added to your PATH during installation)
- **LM Studio**: To set up the local LLM server.
- **Gradio**: Installable via pip within the virtual environment.

### Installation (Windows)

#### 1. Clone the Repository
Open Command Prompt (or PowerShell) and navigate to the directory where you want to clone the repository.

```bash
git clone https://github.com/yourusername/ai-companion.git
cd ai-companion
```

#### 2. Set Up a Virtual Environment
In the project directory, set up a virtual environment to isolate dependencies.

```bash
python -m venv venv
```

This will create a `venv` directory that contains the virtual environment. Next, activate the virtual environment:

- For **Command Prompt**:
  ```bash
  venv\Scripts\activate
  ```
- For **PowerShell**:
  ```bash
  .\venv\Scripts\Activate
  ```

You should see `(venv)` appear before your prompt, indicating the virtual environment is active.

#### 3. Install Dependencies
Once the virtual environment is activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

#### 4. Set Up LM Studio
Download and install **LM Studio** from [the official website](https://lmstudio.ai) and start the local LLM server:

```bash
lmstudio start
```

Ensure it is running on **localhost:1234**.

#### 5. Running the Application
With LM Studio running, launch the Gradio interface by executing the following command:

```bash
python main.py
```

This will start the application. Open your web browser and navigate to the local Gradio interface, usually available at `http://127.0.0.1:7860`.

## File Structure
```
├── api_debugger.py
├── bonding.py
├── chat.py
├── companion_settings.json
├── companion_traits.py
├── create.py
├── main.py
├── new.txt
├── scenario.py
├── settings.py
├── user_info.py
└── yiuyUIt
```

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Thanks to **LM Studio** for providing the local LLM engine.
- Thanks to **Gradio** for the interactive UI framework.
