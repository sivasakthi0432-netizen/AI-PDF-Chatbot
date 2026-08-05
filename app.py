import tempfile
import streamlit as st

from pipeline import process_pdf
from retriever import ask_question

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# --------------------------------------------------
# Session State
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# CSS
# --------------------------------------------------
st.markdown("""
<style>

/* Background */
.stApp{
    background:#0F172A;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#111827;
}

/* Text */
h1,h2,h3,h4,h5,h6,p,label{
    color:white;
}

/* Button */
.stButton>button{
    width:100%;
    background:#2563EB;
    color:white;
    border-radius:10px;
    border:none;
    height:45px;
}

.stButton>button:hover{
    background:#1D4ED8;
}

/* File uploader */
[data-testid="stFileUploader"]{
    background:#1E293B;
    border-radius:10px;
    padding:10px;
}

/* Hide only menu and footer */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:

    st.title("🤖 AI PDF Chatbot")

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if st.button("📚 Process PDF"):

        if uploaded_file is not None:

            with st.spinner("Processing PDF..."):

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as tmp:

                    tmp.write(uploaded_file.getbuffer())
                    pdf_path = tmp.name

                process_pdf(pdf_path)

            st.success("✅ PDF Processed Successfully")

        else:
            st.warning("Please upload a PDF.")

    st.markdown("---")

    if uploaded_file:
        st.success(uploaded_file.name)

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# --------------------------------------------------
# Main Page
# --------------------------------------------------
st.title("🤖 AI PDF Chatbot")

# Display chat history
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------
question = st.chat_input("Ask a question about your PDF...")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = ask_question(
                question,
                st.session_state.messages
            )

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )