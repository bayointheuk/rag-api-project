from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Initialize OpenAI using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# ===== SAMPLE DATA =====
text = """
Webbiit Technologies is a digital training company focused on AI, cybersecurity, and software development.

The company helps students gain practical skills and real-world experience to become job-ready.

It also provides mentorship, internships, and project-based learning programs.
"""

# ===== SPLIT =====
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20)
chunks = splitter.split_text(text)

# ===== EMBEDDINGS =====
embeddings = OpenAIEmbeddings()

# ===== VECTOR DB =====
db = FAISS.from_texts(chunks, embeddings)

# ===== REQUEST MODEL =====
class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "RAG API is running"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    query = request.question

    docs = db.similarity_search(query)
    context = docs[0].page_content

    prompt = f"""
    Answer the question based only on the context below:

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    return {"answer": answer}
