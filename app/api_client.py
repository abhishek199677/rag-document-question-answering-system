import os
import logging
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAIClient:
    def __init__(self):
        # The OpenAI library automatically picks up OPENAI_API_KEY from environment
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")
        self.client = OpenAI()

    def get_embeddings(self, texts, model="text-embedding-3-small"):
        try:
            response = self.client.embeddings.create(
                input=texts,
                model=model
            )
            # OpenAI response contains a 'data' array where each item has an 'embedding'
            return [data.embedding for data in response.data]
        except Exception as e:
            logging.error(f"Error fetching embeddings: {e}")
            raise

    def get_chat_completion(self, messages, model="gpt-3.5-turbo", temperature=0.3):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Error in chat completion: {e}")
            raise
