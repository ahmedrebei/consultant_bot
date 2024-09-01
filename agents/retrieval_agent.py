import json
from loguru import logger
from agents.agent import Agent
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
            # self.chain = self.create_chain(
            #     {
            #         "input_variables": ["user_input"],
            #         "template": """
            #         The user said: {user_input}
            #         """,
            #     }
            # )

        except Exception as e:
            logger.error(f"Error initializing RetrievalAgent: {e}")
            raise

    def get_vectorstore(self, expertise: str):
        embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        chroma_store = ChromaStore(
            collection_name=expertise,
            persist_directory="data/chroma_data",
            embedding_function=embedding,
        )
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
    # def process_input(self, user_input: str):
    #     try:
    #         return self.run(self.chain, user_input=user_input)
    #     except Exception as e:
    #         logger.error(f"Error in RetrievalAgent process_input: {e}")
    #         raise