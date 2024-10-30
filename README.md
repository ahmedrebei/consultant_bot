# Quebec Consulting ChatBot

This is the `README.md` file for your immigration & education Quebec virtual consultant.

# Multi-Agent Chatbot

## Overview

The Multi-Agent Chatbot project leverages multiple agents, including the Retrieval Agent (RAG), to provide accurate and comprehensive answers to user questions about topics related to immigration or education in Quebec. The chatbot is able to retrieve relevant information from a knowledge base and deliver informative responses.


## Project Structure

```
consultant_bot
├── agents
│   ├── agent.py
│   ├── generator_agent.py
│   ├── grading_agent.py
│   ├── greeting_agent.py
│   ├── retrieval_agent.py
│   └── summarization_agent.py
├── data
│   ├── chroma_data
│   ├── chroma_store.py
│   ├── data.json
│   ├── links.json
│   └── scrapper.py
├── config.py
├── Dockerfile
├── README.md
├── requirements.txt
├── run.py
└── workflow.py

```

### Files Description

### Files Description

- **README.md**: The main documentation file for the project.
- **agents**: A directory that contains the implementation of different agents used in the chatbot, including:
    - **agent.py**: Generic agent class that serves as the base for other specialized agents.
    - **generator_agent.py**: Generation agent class.
    - **grading_agent.py**: Grading agent class.
    - **greeting_agent.py**: Greeting agent class.
    - **retrieval_agent.py**: RAG agent class.
    - **summarization_agent.py**: Summarization agent class.

- **config.py**: Get API_KEY from `.env` file.
- **data**: Contains data-related files:
    - **chroma_data**: Directory when Chroma stores the vector store.
    - **chroma_store.py**: Vector store class.
    - **scrapper.py**: scrapping class to scrap input links from `links.json` and store the output in `data.json`
    - **data.json**: Data.
    - **links.json**: Links to scrap.
- **requirements.txt**: List of all the dependencies.
- **workflow.py**: The workflow class of the chatbot.
- **run.py**: The main entry point for running the streamlit application.

![chatbot](https://github.com/user-attachments/assets/79d9d064-29a9-4aca-939c-41dea694fc83)


## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ahmedrebei/consultant_bot
   cd consultant_bot
   ```

2. **Set up environment variables**:
   Create a `.env` file in the root directory with the following content:
   ```env
   OPENAI_API_KEY=...
   ```

## Running the Application Using Docker

1. **Build the Docker Image**:
   ```bash
   docker build -t consultant_bot .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -p 8501:8501 consultant_bot
   ```

## How It Works

The Chatbot project involves several agents that work together to provide accurate and comprehensive answers to user questions. These agents include:

 - **Greeting Agent**: This agent is responsible for ensuring that the user's input is related to the domain knowledge of the chatbot.

 - **Retrieval Agent**: The retrieval agent retrieves relevant chunks of data from the vector store based on the user's query.

 - **Grading Agent**: The grading agent validates the retrieved chunks of data to ensure their accuracy and relevance.

 - **Generator Agent**: The generator agent utilizes the conversation context and the retrieved data to generate informative and contextually appropriate answers.

