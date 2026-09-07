import uuid

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from uuid import uuid4
from pinecone import ServerlessSpec
from pinecone import Pinecone
import dotenv
import os
import json


dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")


embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=api_key,
)


index_name = "data-task-6"  # назва бази даних

pc = Pinecone(api_key=pinecone_api_key)


if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=3072,    # кількість чисел у векторі
        metric="cosine",   # формула для пошуку схожих текстів
        spec=ServerlessSpec(
            cloud="aws",        # хмарна платформа(амазон)
            region="us-east-1"  # регіон
        ),
    )
index = pc.Index(index_name)

vector_store = PineconeVectorStore(
    index=index,
    embedding=embedding
)


with open("data/lesson_rag/huge_file.txt", "r", encoding="utf-8") as f:
    text = f.read()


ids = []
blocks = text.split("\n\n\n")
documents = []


for block in blocks:

    if block.strip():

        document = Document(
            page_content=block.strip()
        )

        documents.append(document)

        ids.append(str(uuid4()))


vector_store.add_documents(
    documents=documents,
    ids=ids
)


with open("data/lesson_rag/ids.json", "w", encoding="utf-8") as file:
    json.dump(ids, file, ensure_ascii=False, indent=2)

print(len(ids))
print(len(documents))
