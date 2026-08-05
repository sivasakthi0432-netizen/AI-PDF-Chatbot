from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient(host="localhost", port=6333)
print(client.get_collections())

COLLECTION_NAME = "pdf_chatbot"

def create_collection():
    collections = client.get_collections().collections

    if COLLECTION_NAME not in [c.name for c in collections]:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )
        print("Collection created")
    else:
        print("Collection already exists")

def get_qdrant_client():
    return client


if __name__ == "__main__":
    create_collection()