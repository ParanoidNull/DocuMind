# 🧠 DocuMind | AI-Powered Document Research Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG-000?logo=chainlink&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991?logo=openai&logoColor=white)

**DocuMind** is a sophisticated **Retrieval-Augmented Generation (RAG)** engine designed to transform static PDF documents into interactive, conversational knowledge bases. By leveraging **OpenAI's LLMs** and **FAISS vector embeddings**, it enables users to query complex documentation with high semantic accuracy and context awareness.

---

## 🏗 Architecture & Tech Stack

The system follows a modern RAG pipeline architecture:

1.  **Ingestion:** Extracts raw text from PDFs using `pypdf`.
2.  **Chunking:** Splits data into semantic chunks via `RecursiveCharacterTextSplitter` to optimize context windows.
3.  **Embedding:** Converts text into high-dimensional vector representations using `OpenAIEmbeddings`.
4.  **Vector Storage:** Indexes vectors locally using **FAISS (Facebook AI Similarity Search)** for millisecond-latency retrieval.
5.  **Inference:** Generates context-aware responses using `gpt-3.5-turbo` via **LangChain**.

---

## 🚀 Key Features

* **Semantic Search:** Goes beyond keyword matching to understand the *intent* behind queries.
* **Context Preservation:** Maintains conversation history for follow-up questions.
* **Source Transparency:** Reduces hallucinations by grounding answers strictly in the provided documents.
* **Secure & Local:** Vector indices are stored locally (`faiss_index`), ensuring efficient reuse without re-processing.

---

## 🛠️ Installation & Setup

### Prerequisites
* Python 3.10 or 3.11
* An active OpenAI API Key

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/DocuMind-AI-Assistant.git](https://github.com/YOUR_USERNAME/DocuMind-AI-Assistant.git)
cd DocuMind-AI-Assistant