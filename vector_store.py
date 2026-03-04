import chromadb
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection("documents")


def create_vector_store(paths):

    for path in paths:

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        chunks = text.split("\n\n")

        for i, chunk in enumerate(chunks):

            embedding = model.encode(chunk).tolist()

            collection.add(
                documents=[chunk],
                embeddings=[embedding],
                metadatas=[{"source": path}],
                ids=[f"{path}_{i}"]
            )