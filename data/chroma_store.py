import json
from langchain_community.vectorstores import Chroma
from typing import List, Dict, Any
from langchain.embeddings.base import Embeddings


class ChromaStore:
    def __init__(
        self,
        collection_name: str,
        persist_directory: str,
        embedding_function: Embeddings,
    ):
        """
        Initializes the ChromaStore with a specific collection name, persistence directory, and embedding function.

        Args:
            collection_name (str): The name of the collection to use in Chroma.
            persist_directory (str): The directory where Chroma will persist its data.
            embedding_function (Embeddings): The embedding function to convert text into vectors.
        """
        self.collection_name = collection_name
        self.persist_directory = persist_directory
        self.embedding_function = embedding_function
        self.vectorstore = Chroma(
            collection_name=collection_name,
            embedding_function=embedding_function,
            persist_directory=persist_directory,
        )

    def add_text_vector_store(self, text_data_dict: dict):
        """
        Adds text data to the vector store.

        Args:
            text_data_dict (dict): A dictionary where the keys are the metadata for the text and the values are the text data.
        """
        for key, value in text_data_dict[self.collection_name].items():
            self.vectorstore.add_texts(texts=value, metadata=key)


    def search(self, query: str, top_k: int = 5):
        """
        Searches the vector store for the top_k most similar documents to the query.

        Args:
            query (str): The query string.
            top_k (int): The number of top results to return. Defaults to 5.

        Returns:
            List[Dict[str, Any]]: A list of the top_k most similar documents.
        """
        results = self.vectorstore.similarity_search(query=query, k=top_k)
        return results

