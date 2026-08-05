from sentence_transformers import SentenceTransformer
from qdrant_client.models import PointStruct
from store_data import get_qdrant_client, COLLECTION_NAME

model = SentenceTransformer("all-MiniLM-L6-v2")
client = get_qdrant_client()

def store_vectors(chunks):
    texts = [chunk.page_content for chunk in chunks]
    embeddings = model.encode(texts)

    points = []

    for i, (text, embedding) in enumerate(zip(texts, embeddings)):
        points.append(
            PointStruct(
                id=i,
                vector=embedding.tolist(),
                payload={"text": text}
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print("✅ Vectors stored successfully")