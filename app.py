from src.services.gemini_service import GeminiService
from src.chatbot.sales_chatbot import SalesChatbot
from src.ui.gradio_ui import launch_gradio_ui

if __name__ == "__main__":
    # Initialize services and chatbot
    try:
        gemini_service = GeminiService()
        sales_chatbot = SalesChatbot(gemini_service=gemini_service)

        # Launch the UI
        print("Launching Gradio UI...")
        launch_gradio_ui(chatbot=sales_chatbot)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure the system prompt file is in the correct location ('prompts/system_message.txt').")
    except ValueError as e:
        print(f"Error: {e}")
        print("Please ensure the GEMINI_API_KEY is set in the .env file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
