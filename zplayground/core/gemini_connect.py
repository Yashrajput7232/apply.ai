
from google import genai
import secrets
import requests
from dotenv import load_dotenv , dotenv_values
import os
load_dotenv()
class Gemini_Connect:

    def __init__(self,agent_name):
        self.agent_name=agent_name
        # self.client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

    def query(self,query):
        client = genai.Client(api_key=os.getenv("API_KEY_GEMINI"))
        response = client.models.generate_content(
        # model="gemini-2.0-flash", contents=query
        model="gemini-2.0-flash", contents=query
        )
        return response.text
        