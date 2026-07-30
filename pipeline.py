from ingest import load_pdf, split_documents
from store_data import create_collection
from vector_store import store_vectors


def process_pdf(pdf_path):
    documents = load_pdf(pdf_path)
    chunks = split_documents(documents)

    create_collection()
    store_vectors(chunks)

    print("✅ PDF Processing Completed")