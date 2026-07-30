from langchain_huggingface import HuggingFaceEmbeddings

# Create embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def get_embedding_model():
    """
    Returns the embedding model
    """
    return embedding_model


if __name__ == "__main__":

    model = get_embedding_model()

    text = "Artificial Intelligence is changing the world."

    vector = model.embed_query(text)

    print(f"Vector Length : {len(vector)}")
    print("\nFirst 10 Values:\n")
    print(vector[:10])