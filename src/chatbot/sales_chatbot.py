import os
from src.services.gemini_service import GeminiService

class SalesChatbot:
    def __init__(self, gemini_service: GeminiService, system_prompt_path: str = 'prompts/system_message.txt'):
        self.gemini_service = gemini_service
        self.system_instruction = self._load_system_prompt(system_prompt_path)
        self.gemini_service.create_chat_session(self.system_instruction)

    def _load_system_prompt(self, file_path: str) -> str:
        try:
            with open(file_path, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            raise FileNotFoundError(f"System prompt file not found at {file_path}")
        except Exception as e:
            raise RuntimeError(f"Error loading system prompt: {e}")

    def chat(self, user_input: str, history):
        # The history parameter is required by Gradio, but the Gemini API handles conversation history internally
        # We just need to send the current user input.
        response_stream = self.gemini_service.send_message_stream(user_input)
        res = ""
        for chunk in response_stream:
            res += chunk.text or ""
            yield res 