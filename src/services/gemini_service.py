import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

class GeminiService:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        self.client = genai.Client(api_key=api_key)
        self.chat_session = None

    def create_chat_session(self, system_instruction: str):
        self.chat_session = self.client.chats.create(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(system_instruction=system_instruction)
        )

    def send_message_stream(self, user_input: str):
        if not self.chat_session:
            raise RuntimeError("Chat session not created. Call create_chat_session first.")
        return self.chat_session.send_message_stream(user_input) 