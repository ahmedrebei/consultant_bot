import json
from loguru import logger
from agents.greeting_agent import GreetingAgent
from agents.retrieval_agent import RetrievalAgent

from langchain_community.embeddings import OpenAIEmbeddings

from config import OPENAI_API_KEY
from data.chroma_store import ChromaStore

class WorkFlow:
    def __init__(self):
        self.greeting_agent = GreetingAgent() #output: "immigration", "education", "other" or "not related"
        self.retrieve_agent = None
        
    def run(self, user_input: str):
        expertise = self.greeting_agent.greet(user_input=user_input)
        if expertise == "not related":
            return 
        elif expertise == 'other':
            return
        else: #immigration or education
            self.retrieve_agent = RetrievalAgent(expertise=expertise)
            search_results = self.retrieve_agent.search(query=user_input, top_k=1)
            for result in search_results:
                print(result)
        


if __name__ == "__main__":
    workflow = WorkFlow()
    user_input = "Je veux ajouter mon epoux a ma demande de residence permanente a Quebec"
    
    workflow.run(user_input=user_input)