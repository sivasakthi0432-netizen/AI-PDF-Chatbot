from embedding import get_embedding_model
from vector_store import get_qdrant_client, COLLECTION_NAME
from llm import generate_answer

# Load embedding model
embedding_model = get_embedding_model()

# Get Qdrant client
client = get_qdrant_client()





def ask_question(question, history):
    docs = retrieve_documents(question)

    print("=" * 50)
    print("Retrieved Documents:", len(docs))

    for i, doc in enumerate(docs):
        print(f"\nDocument {i+1}")
        print(doc.payload)

    return generate_answer(question, docs, history)

def retrieve_documents(query, top_k=5):
    query_vector = embedding_model.embed_query(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k
    )

    print("Retrieved:", len(results.points))

    for point in results.points:
        print(point.payload)

    return results.points