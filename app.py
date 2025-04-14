from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import PyPDF2
import streamlit as st
def prompt(prompt,memory):
    model=ChatGoogleGenerativeAI(api_key="PASTE API KEY HERE",model="gemini-1.5-pro")
    
    idea=PromptTemplate(input_variables=["query","history"],
        template=("""You are a AI chatbot used for answer daily question \n
        you are created by Ravinder Singh  \n
        "Conservational History :{history} \n\n
        "Current query : {query}
        "Answer based on the conservational history and The Current query aur pata nahi chalna chahiye ki tum AI ho , emotions ko samjho insaan ke""")
        )
    chain=LLMChain(llm=model,prompt=idea,memory=memory)
    hist=memory.load_memory_variables(["history"])
    return chain.invoke({"query":prompt,"history":hist["history"]})
def pdf_builder(file,memory):
   
    reader = PyPDF2.PdfReader(file)
        
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    memory.chat_memory.add_ai_message(text.strip())
def main():
    if "mem" not in st.session_state:
        st.session_state.mem = ConversationBufferMemory(memory_key="history")

    mem = st.session_state.mem
    st.sidebar.title("upload Documents to Train")
    st.sidebar.write("Upload the files you wanna need to train it on:-:")
    files=st.sidebar.file_uploader("Choose PDF's only",type=["pdf"],accept_multiple_files=True)
    btn=st.sidebar.button(label="compile")
    if btn==True:
        if files:
            for file in files:
                pdf_builder(file,mem)
            st.sidebar.write("Update_complete:-:?")
    inp="Garuda V1.0"
    st.write("Enter the following queries i am here to help!!")
    st.write(inp)
    val=st.text_input(label="Message Garuda")
    btnn=st.button(label="Generate")
    if val:
       
        # mem.chat_memory.add_user_message(val)
        
        if btnn==True:
            inp=prompt(val,mem)
            st.write(inp["text"])
            st.write(mem.load_memory_variables(["history"]))
            # mem.chat_memory.add_ai_message(inp["text"])           
main()
