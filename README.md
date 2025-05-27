# Sales Chatbot

This project implements a simple sales chatbot with answer streaming using the Google Gemini API and Gradio for the user interface.

![image](https://github.com/user-attachments/assets/64cced34-f040-41ee-abbe-50d25bf71f97)


## Project Structure

```
.
├── prompts/
│   └── system_message.txt
├── src/
│   ├── chatbot/
│   │   └── sales_chatbot.py
│   ├── services/
│   │   └── gemini_service.py
│   └── ui/
│       └── gradio_ui.py
├── app.py
├── requirements.txt
└── README.md
```

- `prompts/`: Contains the system prompt for the chatbot.
- `src/`: Contains the main application logic.
    - `src/services/`: Houses service-related code, like the Gemini API interaction.
    - `src/chatbot/`: Contains the core chatbot logic.
    - `src/ui/`: Contains the code for the user interface.
- `app.py`: The entry point of the application.
- `requirements.txt`: Lists the project dependencies.
- `README.md`: This file.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd Sales-chatbot
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your Google Gemini API Key:**

    - Obtain an API key from the Google AI Studio (https://aistudio.google.com/fundamentals/api_key).
    - Create a `.env` file in the root directory of the project.
    - Add your API key to the `.env` file in the following format:

    ```dotenv
    GEMINI_API_KEY=YOUR_API_KEY
    ```

    Replace `YOUR_API_KEY` with your actual API key.

## Running the Application

1.  Make sure your virtual environment is activated.
2.  Run the `app.py` file:

    ```bash
    python app.py
    ```

3.  A Gradio application will launch, providing a web-based chat interface to interact with the sales chatbot.
