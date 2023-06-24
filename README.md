# Open AI Chatbot

Welcome to the Open AI Chatbot project! This project utilizes the Langchain library to implement a chatbot powered by the OpenAI API.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

To install the Langchain library, follow these steps:

1. Open a terminal or command prompt.

2. Create a virtual environment (optional but recommended):
```shell
python3 -m venv myenv
```

1. Activate the virtual environment:
For Linux/macOS:

```shell

source myenv/bin/activate
```

For Windows:

```shell

    myenv\Scripts\activate
```

Install Langchain using pip:

```shell

    pip install langchain
```
## Configuration

To use the Open AI Chatbot, you need to set your OpenAI API key as an environment variable. Here's how:

- Obtain an API key from the OpenAI website (https://www.openai.com).

- Set the environment variable OPENAI_API_KEY to your API key.
For Linux/macOS:

```shell

export OPENAI_API_KEY=your-api-key
```

For Windows (Command Prompt):

```shell

set OPENAI_API_KEY=your-api-key
```
For Windows (PowerShell):

```shell

        $env:OPENAI_API_KEY="your-api-key"
```
## Usage

You can run the Open AI Chatbot using the provided code snippet. Here's how:

    Make sure you have activated your virtual environment (if applicable).

    Run the chatgpt.py script:

    shell

    python chatgpt.py "your-query"

    Replace "your-query" with the desired query or message you want the chatbot to respond to.

## Additional Notes

    The Langchain library provides various functionalities for document loading, indexing, and working with OpenAI models. Feel free to explore its documentation for more advanced usage.

    Remember to manage your Docker environment if you encounter any issues related to Docker and Docker Compose.

    If you encounter any errors or have questions, please refer to the project's documentation or seek support from the Langchain community.
