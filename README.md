# 🧠 DocuMind | AI-Powered Document Research Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG-000?logo=chainlink&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991?logo=openai&logoColor=white)

**DocuMind** is a sophisticated **Retrieval-Augmented Generation (RAG)** engine designed to transform static PDF documents into interactive, conversational knowledge bases. By leveraging **OpenAI's LLMs** and **FAISS vector embeddings**, it enables users to query complex documentation with high semantic accuracy and context awareness.

---

## 🏗 Architecture & Tech Stack

The system follows a modern RAG pipeline architecture:

1. **Ingestion:** Extracts raw text from PDFs using `pypdf`
2. **Chunking:** Splits data into semantic chunks via `RecursiveCharacterTextSplitter` to optimize context windows
3. **Embedding:** Converts text into high-dimensional vector representations using `OpenAIEmbeddings`
4. **Vector Storage:** Indexes vectors locally using **FAISS (Facebook AI Similarity Search)** for millisecond-latency retrieval
5. **Inference:** Generates context-aware responses using `gpt-3.5-turbo` via **LangChain**

### Technology Stack
- **Frontend:** Streamlit
- **LLM Framework:** LangChain
- **Embeddings:** OpenAI Ada-002
- **Vector Database:** FAISS
- **PDF Processing:** pypdf
- **Language Model:** GPT-3.5-turbo

---

## 🚀 Key Features

- ✅ **Semantic Search:** Goes beyond keyword matching to understand the *intent* behind queries
- ✅ **Context Preservation:** Maintains conversation history for follow-up questions
- ✅ **Source Transparency:** Reduces hallucinations by grounding answers strictly in the provided documents
- ✅ **Secure & Local:** Vector indices are stored locally (`faiss_index`), ensuring efficient reuse without re-processing
- ✅ **Multi-PDF Support:** Process and query multiple PDF documents simultaneously
- ✅ **Real-time Processing:** Instant document indexing and query responses

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10 or 3.11
- An active OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))

### Quick Installation

```bash
# 1. Clone the repository
git clone https://github.com/ParanoidNull/DocuMind-AI-Assistant.git
cd DocuMind-AI-Assistant

# 2. Create & Activate Virtual Environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux:
# python3 -m venv venv
# source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory and add your API key:

```env
OPENAI_API_KEY=sk-your-api-key-here
```

**Note:** You can also enter your API key directly in the Streamlit interface sidebar.

---

## 📦 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit==1.31.0
pypdf==4.0.1
langchain==0.1.10
langchain-community==0.0.24
langchain-openai==0.0.7
langchain-text-splitters==0.0.1
faiss-cpu==1.8.0
python-dotenv==1.0.1
openai==1.12.0
```

---

## 🎯 Usage

### Starting the Application

```bash
# Run with Python module (recommended)
python -m streamlit run app.py

# Or if streamlit is in PATH
streamlit run app.py
```

The application will open automatically in your default browser at `http://localhost:8501`

### Using DocuMind

1. **Enter API Key:** Add your OpenAI API key in the sidebar
2. **Upload PDFs:** Click "Browse files" to upload one or more PDF documents
3. **Process Documents:** Click the "🔄 Process Documents" button
4. **Ask Questions:** Type your questions in the main input field
5. **Get Answers:** Receive AI-generated answers based on your documents

### Example Queries

- "What are the main conclusions of this research paper?"
- "Summarize the methodology section"
- "What data was used in the analysis?"
- "Compare the results from different sections"

---

## 📁 Project Structure

```
DocuMind-AI-Assistant/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys)
├── .gitignore             # Git ignore file
├── README.md              # This file
│
├── faiss_index/           # Generated FAISS vector store (auto-created)
│   ├── index.faiss
│   └── index.pkl
│
└── venv/                  # Virtual environment (not tracked)
```

---

## 🔧 How It Works

### 1. Document Processing Pipeline

```python
PDF Upload → Text Extraction → Text Chunking → Embedding Generation → FAISS Indexing
```

### 2. Query Processing Pipeline

```python
User Query → Embedding Generation → Similarity Search → Context Retrieval → LLM Response
```

### 3. Key Parameters

- **Chunk Size:** 1000 characters
- **Chunk Overlap:** 200 characters
- **Model:** GPT-3.5-turbo
- **Temperature:** 0.3 (lower = more deterministic)
- **Top-K Results:** 3 most relevant chunks

---

## 🔐 Security & Privacy

- **Local Processing:** All vector embeddings are stored locally on your machine
- **API Key Safety:** Never commit `.env` files to version control
- **No Data Retention:** Your documents are processed locally and not sent anywhere except for OpenAI API calls

---

## ⚠️ Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'langchain'`
```bash
Solution: pip install -r requirements.txt
```

**Issue:** `streamlit: command not found`
```bash
Solution: python -m streamlit run app.py
```

**Issue:** Import errors with langchain
```bash
Solution: 
pip uninstall langchain langchain-community langchain-openai -y
pip install langchain langchain-community langchain-openai
```

**Issue:** FAISS index not found
```bash
Solution: Upload and process documents first before asking questions
```

---

## 🚧 Limitations

- Only supports PDF files (not DOCX, TXT, or other formats)
- Limited by OpenAI API rate limits and costs
- Context window limited to GPT-3.5-turbo's maximum tokens
- Best suited for English documents (multilingual support varies)

---

## 🛣️ Roadmap

- [ ] Support for DOCX, TXT, and other document formats
- [ ] Multi-language support
- [ ] Persistent chat history
- [ ] Export conversation to PDF/TXT
- [ ] Advanced filtering and document management
- [ ] Integration with GPT-4 for enhanced accuracy
- [ ] Cloud deployment option

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@ParanoidNull](https://github.com/ParanoidNull)

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [LangChain](https://python.langchain.com/) - For RAG orchestration
- [OpenAI](https://openai.com/) - For GPT models and embeddings
- [FAISS](https://github.com/facebookresearch/faiss) - For efficient similarity search

---


<div align="center">

**⭐ If you find this project helpful, please consider giving it a star! ⭐**

Made with ❤️ using Python, Streamlit & LangChain

</div>