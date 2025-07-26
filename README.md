# RAG-Chatbot

**A modular Retrieval-Augmented Generation (RAG) chatbot built with FastAPI, Streamlit, and ChromaDB.**

## Overview

RAG-Chatbot is designed to answer user questions based on custom document datasets. It integrates retrieval-based search with generative AI, providing accurate and context-aware responses. The backend is powered by FastAPI for performance, ChromaDB for vector storage, and Streamlit offers a user-friendly web interface.

## Features

- **Retrieval-Augmented Generation**: Combines document retrieval with LLM-based answer generation.
- **FastAPI Backend**: High-performance REST API for core RAG operations.
- **Streamlit UI**: Simple, extensible interface for user interactions.
- **ChromaDB**: Efficient storage and search of embeddings for fast document retrieval.
- **Modular Design**: Easily extend or replace components.

## Architecture

- **FastAPI**: Backend API endpoints for document upload, search, and chat operations.
- **Streamlit**: Frontend for user interaction and result display.
- **ChromaDB**: Stores vector embeddings of uploaded documents.
- **LLM Integration**: Connects to local or cloud-hosted large language models for answer generation.

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Optionally: a GPU (for local LLM inference)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Dev-W32/RAG-Chatbot.git
   cd RAG-Chatbot
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **(Optional) Set up your LLM credentials/configs:**
   - You may need an API key for OpenAI, Huggingface, or configure your local LLM path.

### Usage

#### Start the Backend API

```sh
uvicorn app.main:app --reload
```

#### Launch the Streamlit UI

```sh
streamlit run ui/app.py
```

#### Upload and Chat

- Upload your documents (supported formats: PDF, TXT, Markdown, DOCX).
- Enter your questions in the chat interface—answers include citation to relevant document sections for transparency.

## Configuration

- **Embedding model**: Easily swappable to fit your accuracy/performance needs.
- **ChromaDB**: Can be configured for persistent storage.
- **LLM model**: Plug in your preferred language model.

## Folder Structure
```
RAG-CHATBOT-FASTAPI/
├── client/
│   ├── components/
│   │   ├── chatui.py
│   │   ├── history_download.py
│   │   └── upload.py
│   └── utils/
│       ├── api.py
│       ├── app.py
│       └── config.py
├── server/
│   ├── chroma_store/
│   ├── modules/
│   │   ├── llm.py
│   │   ├── load_vectorstore.py
│   │   ├── pdf_handlers.py
│   │   └── query_handlers.py
│   ├── uploaded_pdfs/
│   └── logger.py
├── venv/
├── .env
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Roadmap / TODO

- [ ] Add support for additional file formats.
- [ ] Improve multi-turn conversation handling.
- [ ] Integrate more LLMs and embedding models.
- [ ] Deployment with Docker.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License.

**Note:**  
This README is based on best practices and standard RAG chatbot setups[6][2][3]. For specific configuration, file paths, or advanced options, consult the source code and in-repo documentation (if provided). If you have access to the actual codebase, adjust interface endpoints or model specifications as necessary.

[1] https://github.com/Dev-W32/RAG-Chatbot
[2] https://github.com/ZeusSama0001/RAG-chatbot
[3] https://github.com/umbertogriffo/rag-chatbot
[4] https://github.com/vitorccmanso/Rag-ChatBot
[5] https://github.com/AlaGrine/RAG_chatabot_with_Langchain
[6] https://github.com/cloudxlab/RAG-Chatbot-from-web-data/blob/master/README.md
[7] https://github.com/rumeysacelik/RAG-Project/blob/new-branch/README.md
[8] https://github.com/pymupdf/RAG
[9] https://www.datacamp.com/projects/2041
[10] https://github.com/umbertogriffo/rag-chatbot/blob/main/README.md
[11] https://codebase.helmholtz.cloud/f.doering/rag-chatbot/-/blob/b0f28dca4abcfe5b7bb2ae908fe4e771a1bcfa2d/README.md