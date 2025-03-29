# Garuda - WhatsApp-Style AI Chatbot

Garuda is a mental health chatbot built using **LangChain**, **Google Gemini AI**, and **Streamlit**. It allows users to interact with the AI in a **WhatsApp-style chat interface**, with persistent conversation history. Additionally, users can upload **PDFs** to train the AI with external knowledge.

---

## Features 🚀
✅ **WhatsApp-style chat UI** with past conversations visible 📱  
✅ **Conversational memory** using `st.session_state.messages` 🧠  
✅ **Google Gemini AI integration** for intelligent responses 🤖  
✅ **PDF training support** to enhance AI knowledge 📂  
✅ **Secure API key usage** via environment variables 🔐  

---

## Installation & Setup 🛠️

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/garuda-chatbot.git
cd garuda-chatbot
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.8+** installed. Then, install the required libraries:
```bash
pip install streamlit langchain-google-genai PyPDF2
```

### 3️⃣ Set Up Environment Variables
Create an `.env` file or set the API key manually:
```bash
export GEMINI_API_KEY="your_google_gemini_api_key"
```
For Windows (Command Prompt):
```cmd
set GEMINI_API_KEY=your_google_gemini_api_key
```

---

## Usage 🏃‍♂️

### Run the Chatbot
```bash
streamlit run app.py
```

### Upload PDFs to Train AI
1️⃣ Click on **'Upload PDFs to Train AI'** in the sidebar.  
2️⃣ Choose one or more `.pdf` files.  
3️⃣ Click **'Train AI'**, and the content will be stored in memory. ✅  

### Chat with Garuda 🤖
1️⃣ Type a message in the chat input.  
2️⃣ Get instant responses with emotional intelligence.  
3️⃣ See previous questions and answers in a WhatsApp-style UI.  

---

## Folder Structure 📂
```
📂 Garuda Chatbot
├── app.py              # Main application file
├── README.md           # Project documentation
├── requirements.txt    # Dependencies list
└── .env                # API keys (not included in repo)
```

---

## Future Improvements 🔥
✅ Add voice input & response 📢  
✅ Implement multi-user sessions 🏷️  
✅ Support for other document formats (TXT, DOCX) 📄  

---

## License 📜
This project is licensed under the **MIT License**.

---

## Contact & Support ✉️
For any questions, reach out at **your.email@example.com** or open an issue on GitHub!

---

Happy Chatting! 🎉

