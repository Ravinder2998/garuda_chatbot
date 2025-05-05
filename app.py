from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import PyPDF2
import streamlit as st

# Function to generate chatbot response
def prompt(prompt, memory):
    model = ChatGoogleGenerativeAI(api_key="WRITE API KEY HERE", model="gemini-1.5-pro")
    
    idea = PromptTemplate(
        input_variables=["query", "history"],
        template=(""" 
        You are an AI chatbot created by Ravinder Singh.\n
        Conservational History: {history}\n\n
        Current query: {query}\n
        Answer based on the conservational history and the current query.\n
        Keep your answers short, concise, and to the point.\n
        Avoid long explanations, make sure it feels like a human interaction. 
        """)
    )
    
    chain = LLMChain(llm=model, prompt=idea, memory=memory)
    hist = memory.load_memory_variables(["history"])
    return chain.invoke({"query": prompt, "history": hist["history"]})

# Function to extract text from PDF and add to memory
def pdf_builder(file, memory):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    memory.chat_memory.add_ai_message(text.strip())

# Main function
def main():
    st.set_page_config(page_title="Garuda Chatbot", page_icon="🤖")
    
    # Apply custom background color
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #111111;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.title("🤖 Garuda V1.0 – Your Personal Assistant")

    if "mem" not in st.session_state:
        st.session_state.mem = ConversationBufferMemory(memory_key="history")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    mem = st.session_state.mem

    st.sidebar.title("📁 Upload Documents")
    st.sidebar.write("Upload PDFs to train the chatbot:")
    files = st.sidebar.file_uploader("Choose PDF files", type=["pdf"], accept_multiple_files=True)
    compile_btn = st.sidebar.button(label="Compile PDFs")

    if compile_btn:
        if files:
            for file in files:
                pdf_builder(file, mem)
            st.sidebar.success("✅ PDF Data Added to Chatbot Memory")

    # Display chat bubbles styled like WhatsApp/Instagram
    st.write("---")
    for sender, message in st.session_state.chat_history:
        if sender == "user":
            st.markdown(
                f"""
                <div style='text-align: right;'>
                    <div style='display: inline-block; background-color: #d3f8d3; color: black; padding: 10px 15px; margin: 5px; border-radius: 10px 0px 10px 10px; max-width: 70%;'>
                        {message}
                    </div>
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style='text-align: left;'>
                    <div style='display: inline-block; background-color: #eee6dd; color: black; padding: 10px 15px; margin: 5px; border-radius: 0px 10px 10px 10px; max-width: 70%;'>
                        {message}
                    </div>
                </div>
                """, unsafe_allow_html=True
            )

    # WhatsApp-like input area
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your message...", key="input_text", placeholder="Write a message…")
        submitted = st.form_submit_button("📩 Send")

    if submitted and user_input:
        st.session_state.chat_history.append(("user", user_input))
        response = prompt(user_input, mem)
        bot_reply = response["text"]
        st.session_state.chat_history.append(("bot", bot_reply))
        st.rerun()

main()
