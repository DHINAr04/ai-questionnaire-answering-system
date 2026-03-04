import os
import chromadb
from sentence_transformers import SentenceTransformer

# embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# persistent chroma database
client = chromadb.PersistentClient(path="vector_db")
collection = client.get_or_create_collection("documents")


def generate_answer(question):

    query_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    docs = results["documents"][0]
    metadata = results["metadatas"][0]
    distances = results["distances"][0]

    if len(docs) == 0:
        return "Not found in references.", "No supporting evidence found.", "—", 0

    snippet = docs[0]

    # ---------- find best sentence ----------
    sentences = snippet.split(".")

    best_sentence = sentences[0]
    best_score = -1

    for sentence in sentences:

        if len(sentence.strip()) < 5:
            continue

        s_emb = model.encode(sentence).tolist()
        q_emb = query_embedding

        # cosine similarity
        score = sum([a*b for a,b in zip(q_emb,s_emb)])

        if score > best_score:
            best_score = score
            best_sentence = sentence

    answer = best_sentence.strip() + "."

    citation = os.path.basename(metadata[0]["source"])

    # ---------- confidence ----------
    distance = distances[0]

    # Convert distance to similarity
    similarity = 1 / (1 + distance)

    confidence = int(similarity * 100)

    confidence = max(40, min(confidence, 95))

    return answer, snippet, citation, confidence