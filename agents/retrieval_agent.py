import json
from typing import List
from loguru import logger
from agents.agent import Agent
from agents.grading_agent import GradingAgent
from config import OPENAI_API_KEY

from langchain_community.embeddings import OpenAIEmbeddings

from data.chroma_store import ChromaStore

class RetrievalAgent(Agent):
    def __init__(self, expertise: str):
        try:
            super().__init__()
            self.expertise = expertise
            if self.expertise not in ["education", "immigration"]:
                raise ValueError("Invalid expertise. Allowed values are 'education' or 'immigration'.")
            self.vectorstore = self.get_vectorstore(expertise=self.expertise)
            
            self.grader = GradingAgent(expertise=self.expertise)

        except Exception as e:
            logger.error(f"Error initializing RetrievalAgent: {e}")
            raise

    def get_vectorstore(self, expertise: str):
        embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        chroma_store = ChromaStore(
            collection_name=expertise,
            persist_directory=f"data/chroma_data/{expertise}",
            embedding_function=embedding,
        )

        if chroma_store.vectorstore._collection.count():
            return chroma_store
        
        with open("data/data.json", "r") as file:
            data_dict = json.load(file)
        chroma_store.add_text_vector_store(data_dict)
        return chroma_store
        
    def search(self, query: str, top_k: int = 5):
        try:
            results = self.vectorstore.search(query=query, top_k=top_k)
            return results
        except Exception as e:
            logger.error(f"Error in RetrievalAgent search: {e}")
            raise
    
    def grade(self, query: str, documents: List[str]):
        try:
            return [self.grader.grade(query=query, retrieved_data=document) for document in documents]
        except Exception as e:
            logger.error(f"Error in RetrievalAgent grade: {e}")
            raise
        
        
    def execute(self, query: str, top_k: int = 5):
        try:
            filtered_documents = []
            search_results = self.search(query=query, top_k=top_k)
            graded_results = self.grade(query=query, documents=search_results)
            
            for result, grade in zip(search_results, graded_results):
                if grade == "true":
                    
                    filtered_documents.append(result)
            return filtered_documents
                
        except Exception as e:
            logger.error(f"Error in RetrievalAgent execute: {e}")
            raise