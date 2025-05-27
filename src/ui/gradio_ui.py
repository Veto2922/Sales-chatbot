import gradio as gr
from src.chatbot.sales_chatbot import SalesChatbot

def launch_gradio_ui(chatbot: SalesChatbot):
    """
    Launches the Gradio chat interface.

    Args:
        chatbot: An instance of the SalesChatbot class.
    """
    gr.ChatInterface(fn=chatbot.chat).launch() 