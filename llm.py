import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")

if not groq_key:
    raise ValueError("GROQ_API_KEY not found")


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=groq_key,
    temperature=0
)


def generate_answer(question, docs, history):

    if not docs:
        return "❌ No relevant information found."

    context = "\n\n".join(
        doc.payload.get("text", "")
        for doc in docs
    )

    chat_history = ""

    for msg in history:
        chat_history += f"{msg['role']}: {msg['content']}\n"


    prompt = f"""
You are an AI assistant.

Conversation:
{chat_history}

PDF Context:
{context}

Question:
{question}

Answer only from the PDF context.
If the answer is not available, say:
"I couldn't find the answer in the uploaded PDF."
"""


    try:
        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"❌ Groq Error: {e}"