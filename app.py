import os
import streamlit as st
import PyPDF2
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

# Function to interact with Gemini AI
def prompt(user_query, memory):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("API Key not found! Set GEMINI_API_KEY environment variable.")

    model = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-1.5-pro", temperature=0.7)

    idea = PromptTemplate(
        input_variables=["query", "history"],
        template="""
        You are Garuda, a mental health AI created by TechSyndicate.
        Conversational History: {history}
        Current Query: {query}
        Provide a thoughtful and emotionally intelligent response.
        """
    )

    chain = LLMChain(llm=model, prompt=idea, memory=memory)

    hist = memory.load_memory_variables({})
    response = chain.invoke({"query": user_query, "history": hist.get("history", "")})

    return response.get("output_text", "I'm sorry, I couldn't generate a response.")

# Function to extract text from PDFs
def pdf_builder(file, memory):
    reader = PyPDF2.PdfReader(file)
    text = ""
    
    for page in reader.pages:
        extracted_text = page.extract_text()
        text += extracted_text if extracted_text else "[No Text Found]"

    memory.chat_memory.add_ai_message(text.strip())

# Streamlit UI
def main():
    st.sidebar.title("Upload PDFs to Train AI")
    if "mem" not in st.session_state:
        st.session_state.mem = ConversationBufferMemory(memory_key="history")

    mem = st.session_state.mem

    files = st.sidebar.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
    if st.sidebar.button("Train AI") and files:
        for file in files:
            pdf_builder(file, mem)
        st.sidebar.success("Training Complete ✅")

    # Display chat messages from history on app rerun
    st.title("📱 Garuda - WhatsApp Style Chatbot")
    
    # Initialize chat history in session state if not already
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input field for user
    user_input = st.chat_input("Type your message...")
    if user_input:
        # Display user message in chat
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate response
        response_text = prompt(user_input, mem)

        # Display AI response in chat
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        with st.chat_message("assistant"):
            st.markdown(response_text)

if __name__ == "__main__":
    main()
