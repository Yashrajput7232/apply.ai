from google import genai
from dotenv import load_dotenv 
import os

load_dotenv('.env')
API_key = os.getenv('API_KEY')
if not API_key:
    raise ValueError('API_KEY not found in .env file')
else:
    print('API_KEY found')
class AIEngine:
    def __init__(self,agent_name):
        self.agent_name = agent_name
        self.api_key = API_key
        self.client = genai.Client(api_key=API_key)
        self.memory = {}
        self.memory['instrucions']=''''''
        print(f'AI Engine: {self.agent_name}')
    
    def generate_content(self, prompt, model="gemini-2.0-flash"):
        """Generate content using the specified model"""
        print(f'Generating content using model: {model}')
        response = self.client.models.generate_content(
            model=model, 
            contents=prompt
        )
        return response.text
    def store_memory(self, key, value):
        """Store a memory value"""
        print(f'Storing memory: {key}')
        self.memory[key] = value
    
    def get_agent_name(self):
        print(f'Getting agent name: {self.agent_name}')
        """Return the agent name"""
        return self.agent_name
    
    def retrieve_memory(self, key):
        print(f'Retrieving memory: {key}')
        """Retrieve information from agent's memory"""
        return self.memory.get(key, None)
    
    def __str__(self):
        return  f'AI Engine: {self.agent_name}'
    

    
