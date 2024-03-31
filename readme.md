# LangChain Chat - GitHub Repository

Welcome to the LangChain Chat GitHub repository! LangChain Chat is a language model-based chat application built using OpenAI's GPT models and Hugging Face's Transformers library. This README will guide you through the installation process and running the application.

## Installation

To install LangChain Chat, follow these steps:

1. Ensure you have the necessary environment set up.
2. Clone this repository to your local machine.
3. Navigate to the cloned repository directory.
4. Run the following command in your terminal to install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, you need to configure the API keys. Follow these steps:

1. Navigate to the `src` directory.
2. Open the `secrets.py` file.
3. Fill in the placeholders for the OpenAI API key and Hugging Face API key with your respective API keys.

```python
# src/secrets.py

# Fill in your OpenAI API key here
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Fill in your Hugging Face API key here
HUGGINGFACE_API_KEY = "YOUR_HUGGINGFACE_API_KEY"
```

## Usage

To run LangChain Chat, follow these steps:

1. Ensure your virtual environment is activated.
2. Navigate to the root directory of the repository.
3. Run the following command in your terminal:

```bash
streamlit run main.py
```

This command will start the Streamlit application, and you'll be able to interact with LangChain Chat in your web browser.

## Additional Information

LangChain Chat leverages the power of OpenAI's language models to provide conversational capabilities. It uses Hugging Face's Transformers library for model loading and inference.

For any issues or suggestions, feel free to open an issue on GitHub or contact us directly.

Thank you for using LangChain Chat!

## License

This project is licensed under the [MIT License](LICENSE).
