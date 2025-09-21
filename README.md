# Gemini Language Translator 🌍

A simple yet powerful language translation web application built with **Streamlit** and powered by **Google's Gemini API**. This tool allows you to translate any text into a wide variety of languages quickly and easily.

[](https://www.python.org/)
[](https://streamlit.io/)
[](https://www.google.com/search?q=https://ai.google/gemini/)

-----

## Demo

Here's a quick look at the application in action:

<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/f58a1588-342b-4bb2-8952-778c7c7307a5" />


-----

## Features ✨

  - **Seamless Translation**: Translate text into any language supported by Google Gemini.
  - **Simple UI**: Clean and intuitive user interface built with Streamlit.
  - **Fast & Accurate**: Leverages the power of the `gemini-1.5-flash-latest` model for high-quality translations.
  - **Easy to Setup**: Get the application running locally in just a few simple steps.

-----

## Tech Stack 🛠️

  - **Frontend**: Streamlit
  - **Backend & AI**: Google Gemini API (`google-generativeai`)
  - **Language**: Python
  - **Environment Management**: `python-dotenv`

-----

## Setup and Installation 🚀

Follow these steps to get the project running on your local machine.

### Prerequisites

  - Python 3.8 or higher installed.
  - A **Google AI API Key**. You can obtain one for free from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation Steps

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/gemini-language-translator.git
    cd gemini-language-translator
    ```

2.  **Create and activate a virtual environment:**

      - **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
      - **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required dependencies:**
    Create a file named `requirements.txt` in the project's root directory with the following content:

    ```
    streamlit
    google-generativeai
    python-dotenv
    ```

    Then, run this command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    Create a file named `.env` in the root of your project directory. Add your Google API key to this file:

    ```
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
    ```

5.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    Your web browser should automatically open to `http://localhost:8501`, where the application is running.

-----

## How to Use 📝

1.  Enter the text you wish to translate into the **"Enter text to translate"** input field.
2.  Specify the language you want to translate to (e.g., "Hindi", "Spanish", "French") in the **"Translate to"** input field.
3.  Click the **"Translate"** button.
4.  The translated text will appear below in a green success box.

-----

## Code Overview 🧑‍💻

The application logic is contained within `app.py`:

  - **Streamlit (`st`)**: Used to create the web interface, including the title, text inputs, and button.
  - **Dotenv (`load_dotenv`)**: Loads the `GOOGLE_API_KEY` from the `.env` file securely.
  - **Google Generative AI (`genai`)**: Configured with the API key to interact with the Gemini model.
  - **Prompt Engineering**: When the "Translate" button is clicked, a carefully crafted prompt is sent to the Gemini API, instructing it to translate the given text and return *only* the translation, without any extra commentary or explanations.
  - **Error Handling**: A `try...except` block is included to catch and display potential errors from the API.

-----

## Contributing 🤝

Contributions are welcome! If you have suggestions for improvements or find a bug, please feel free to open an issue or submit a pull request.

-----

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for more details.
