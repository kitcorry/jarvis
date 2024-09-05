# JARVIS - Langchain Voice Assistant Project

This Voice Assistant project leverages the power of the OpenAI GPT model, pyttsx3 for text-to-speech, speech_recognition for converting spoken language into text, and python-dotenv for managing environment variables. It's designed to provide an interactive and conversational AI experience, inspired by Jarvis from the Iron Man series.

## Features

- **Dynamic Conversations**: Utilizes `langchain` and `langchain_openai` for complex and coherent chat capabilities.
- **Customizable Settings**: Configure model, voice, volume, and more via command-line arguments or environment variables.
- **Session Management**: Supports dynamic session IDs for managing conversation history.
- **Speech Recognition**: Includes phrase time limit settings for improved responsiveness.

## Requirements

- Python 3.7+
- An OpenAI API key

## Installation

Before you begin, ensure you have Python installed on your system. Then, clone this repository and navigate into the project directory.

1. **Clone the Repository**

```bash
git clone https://github.com/kitcorry/jarvis
cd jarvis
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

If the `speech_recognition` package didn't install successfully, alternatively you can install the package directly from the source code by cloning the Git repository and running the setup.py script:
```
git clone https://github.com/Uberi/speech_recognition.git
cd speech_recognition
python setup.py install
```

## Usage

Run the assistant using the following command:

```bash
python jarvis.py
```

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
