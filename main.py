from src.services.gemini_service import GeminiService
from src.chatbot.sales_chatbot import SalesChatbot
from src.ui.gradio_ui import launch_gradio_ui

if __name__ == "__main__":
    # Initialize services and chatbot
    gemini_service = GeminiService()
    sales_chatbot = SalesChatbot(gemini_service=gemini_service)

    # Launch the UI
    print("Launching Gradio UI...")
    launch_gradio_ui(chatbot=sales_chatbot)
