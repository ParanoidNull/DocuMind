import streamlit as st
from pypdf import PdfReader
import os
from dotenv import load_dotenv

# --- Modern LangChain Importları (Düzeltilmiş) ---
try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    from langchain_community.vectorstores import FAISS
    
except ImportError as e:
    st.error(f"Kritik Kütüphane Hatası: {e}")
    st.error("Lütfen şu komutu çalıştırın: python -m pip install langchain langchain-community langchain-openai pypdf python-dotenv streamlit faiss-cpu")
    st.stop()

# --- Configuration & Setup ---
load_dotenv()

# Streamlit Page Config
st.set_page_config(
    page_title="DocuMind | AI Research Assistant",
    page_icon="🧠",
    layout="wide"
)

# --- Core Functions ---

def extract_text_from_pdf(pdf_docs):
    """
    PDF dosyalarından ham metni çıkarır.
    """
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

def get_text_chunks(text):
    """
    Metni işlenebilir parçalara böler.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def create_vector_store(text_chunks, api_key):
    """
    Embedding oluşturur ve FAISS veritabanına kaydeder.
    """
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    return vector_store

def process_user_input(user_question, api_key):
    """
    Kullanıcı sorusunu işler ve cevap döndürür.
    Modern ve basit yaklaşım - load_qa_chain kullanmıyor.
    """
    try:
        embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        
        # FAISS veritabanını yükle
        new_db = FAISS.load_local(
            "faiss_index", 
            embeddings, 
            allow_dangerous_deserialization=True
        )
        
        # En alakalı 3 dokümanı bul
        docs = new_db.similarity_search(user_question, k=3)
        
        # LLM'i başlat
        llm = ChatOpenAI(
            model="gpt-3.5-turbo", 
            temperature=0.3, 
            openai_api_key=api_key
        )
        
        # Context'i birleştir
        context = "\n\n---\n\n".join([doc.page_content for doc in docs])
        
        # Prompt oluştur
        prompt = f"""Aşağıdaki bağlam bilgisine dayanarak soruyu yanıtla. 
Eğer cevabı bağlamda bulamazsan, bilmediğini söyle. Uydurma.

BAĞLAM:
{context}

SORU: {user_question}

CEVAP:"""
        
        # Cevabı al
        response = llm.invoke(prompt)
        
        return response.content
        
    except Exception as e:
        raise Exception(f"İşlem hatası: {str(e)}")

# --- Main UI Logic ---

def main():
    st.header("🧠 DocuMind: Chat with your Documents")
    
    # Sidebar
    with st.sidebar:
        st.title("⚙️ Settings")
        st.markdown("---")
        
        api_key = st.text_input(
            "OpenAI API Key", 
            type="password", 
            help="Enter your OpenAI API key (starts with sk-)"
        )
        
        st.subheader("📄 Your Documents")
        pdf_docs = st.file_uploader(
            "Upload PDFs here and click 'Process'", 
            accept_multiple_files=True,
            type=['pdf']
        )
        
        if st.button("🔄 Process Documents", use_container_width=True):
            if not api_key:
                st.error("⚠️ Please enter your OpenAI API Key first.")
            elif not pdf_docs:
                st.warning("⚠️ Please upload at least one PDF.")
            else:
                with st.spinner("🔍 Analyzing documents... This may take a moment."):
                    try:
                        # 1. Extract
                        raw_text = extract_text_from_pdf(pdf_docs)
                        
                        if not raw_text.strip():
                            st.error("❌ No text could be extracted from the PDFs.")
                            return
                        
                        # 2. Split
                        text_chunks = get_text_chunks(raw_text)
                        st.info(f"📊 Created {len(text_chunks)} text chunks")
                        
                        # 3. Vectorize
                        create_vector_store(text_chunks, api_key)
                        
                        st.success("✅ Indexing Complete! You can now ask questions.")
                        
                    except Exception as e:
                        st.error(f"❌ Processing Error: {e}")
        
        # Info box
        with st.expander("ℹ️ How to use"):
            st.markdown("""
            1. Enter your OpenAI API key
            2. Upload one or more PDF files
            3. Click 'Process Documents'
            4. Ask questions about your documents
            """)

    # Main Chat Area
    st.markdown("### 💬 Ask Questions")
    user_question = st.text_input(
        "Type your question here:",
        placeholder="e.g., What are the main points discussed in the document?"
    )

    if user_question:
        if not api_key:
            st.error("🔑 API Key is missing. Please enter it in the sidebar.")
        elif not os.path.exists("faiss_index"):
            st.warning("📁 Please upload and process documents first.")
        else:
            with st.spinner("🤔 Thinking..."):
                try:
                    response = process_user_input(user_question, api_key)
                    
                    st.markdown("### 📝 Answer")
                    st.write(response)
                    
                    with st.expander("🔍 View Source Context"):
                        st.info("The answer was derived from the most relevant sections of your uploaded PDF documents.")
                        
                except Exception as e:
                    st.error(f"❌ An error occurred: {e}")
                    st.info("💡 Tip: Make sure your API key is valid and you have processed documents first.")

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>Made with ❤️ using Streamlit & LangChain</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()