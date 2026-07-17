import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

#membaca API Key dari .env
load_dotenv()

#membaca PDF
loader = PyPDFLoader("data/1810.04805.pdf")
dokumen = loader.load()

#melakukan chunking
pemecah_teks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
potongan_teks = pemecah_teks.split_documents(dokumen)

#membuat embedding
embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

#menyimpan vector store
vector_store = Chroma.from_documents(
    documents=potongan_teks, 
    embedding=embedding, 
    persist_directory="chroma_db"
)

#membuat retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

#membuat prompt
template = """You are a helpful assistant.

Answer ONLY based on the provided context.

If the answer is not in the context, reply:

"Saya tidak tahu. Informasi tersebut tidak terdapat pada dokumen."

Always answer in Indonesian, even if the document is in English.

At the end, mention the source page.

Context: {context}
Question: {question}
"""
prompt = PromptTemplate.from_template(template)

def gabung_dokumen(docs):
    hasil = []
    for doc in docs:
        halaman = doc.metadata.get('page', 0) + 1
        hasil.append(f"Teks: {doc.page_content}\nHalaman: {halaman}")
    return "\n\n".join(hasil)

#membuat rag chain
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
rag_chain = (
    {"context": retriever | gabung_dokumen, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("===================================")
print("CHATBOT RAG PDF")
print("===================================")
print("Ketik pertanyaan atau ketik exit untuk keluar.\n")

#loop chatbot
while True:
    pertanyaan = input("Pertanyaan:\n> ")
    if pertanyaan.lower() == "exit":
        break
        
    jawaban = rag_chain.invoke(pertanyaan)
    print(jawaban)
    print("\n")
