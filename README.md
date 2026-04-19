# 🤖 AI RAG Assistant API (Webbiit Knowledge System)

## 🚀 Overview
This project is a production-style **Retrieval-Augmented Generation (RAG) AI system** that answers questions using a custom knowledge base.

It combines:
- Large Language Models (LLMs)
- Vector search (FAISS)
- API deployment (FastAPI + Render)

The system is designed to simulate how companies build **AI-powered assistants for internal knowledge, customer support, and business intelligence**.

---

## 🌐 Live API
👉 https://rag-api-project-r987.onrender.com/docs

---

## ⚙️ Tech Stack

- Python
- FastAPI (API backend)
- OpenAI (LLM)
- LangChain (RAG pipeline)
- FAISS (vector database)
- Render (cloud deployment)

---

## 🧠 How It Works (Architecture)

1. Data is loaded (text / PDFs / web content)
2. Content is split into chunks
3. Chunks are converted into embeddings
4. Stored in FAISS vector database
5. User asks a question via API
6. System retrieves relevant context
7. LLM generates accurate answer

---

## 📡 API Endpoint

### POST `/ask`

---

## 📥 Example Input

```json
{
  "question": "What does Webbiit Technologies do?"
}
EXAMPLE OUTPUT
{
  "answer": "Webbiit Technologies is a digital training company focused on AI, cybersecurity, and software development..."
}

💡 Use Cases
AI knowledge assistants
Customer support automation
Internal company documentation search
EdTech AI tutors
Business intelligence systems

🔥 Key Features
Retrieval-Augmented Generation (RAG)
Real-time question answering
Context-aware responses
Scalable API architecture
Cloud deployment (Render)

📁 Project Structure
rag-api-project/
│
├── rag_app.py
├── requirements.txt
└── README.md

🧪 How to Run Locally
pip install -r requirements.txt
uvicorn rag_app:app --reload

🔐 Environment Variables

Set your OpenAI key:

OPENAI_API_KEY=your_api_key_here

👨‍💻 Author

Ajayi Adebayo

AI Engineer (ML + LLM Systems)
MSc Artificial Intelligence (UK)
🚀 Next Improvements
PDF knowledge base integration
Website scraping automation
Chat memory (conversation history)
Frontend (ChatGPT-style UI)
WhatsApp / Telegram AI bot
📌 Summary

This project demonstrates the ability to:

✔ Build LLM-powered systems
✔ Implement RAG architecture
✔ Design and deploy APIs
✔ Work with real-world AI pipelines
