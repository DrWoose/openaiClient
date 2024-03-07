# openaiBot README

## Overview

The `openaiBot` class provides a simple interface to interact with OpenAI's GPT models. It encapsulates the process of sending messages to the model and receiving responses, allowing for an easier integration of OpenAI's capabilities into Python applications.

## Features

- **Token Tracking:** Keeps track of the number of tokens used in prompts and completions, helping manage API usage and costs.
- **Stateless Option:** Can operate in a stateless mode, where the chat history isn't preserved between messages, allowing for independent interactions.
- **JSON Mode:** Offers an option to receive responses in JSON format, facilitating the processing of structured data.
- **Customizable Settings:** Allows setting parameters like the AI model, the initial prompt (job), temperature, and token limits to tailor the behavior of the AI.

## Installation

To use `openaiBot`, ensure you have the `openai` library installed:

```
pip install openai
```

## Usage

1. **Initialization:**

```python
from openaiBot import openaiBot

bot = openaiBot(api_key="your_api_key_here")
```

2. **Sending a Message to the AI:**

```python
response = bot.chat("Hello, how can I help you today?")
print(response)
```

3. **Resetting the Chat:**

```python
bot.reset_chat()
```

4. **Token Usage Information:**

```python
bot.show_tokens()
```

## Dependencies

- `openai` Python library
- `json` for JSON handling
