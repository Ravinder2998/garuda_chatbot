# 🤖 Garuda V1.0 – Your Personal Assistant

Garuda is an AI-powered chatbot built using [LangChain](https://www.langchain.com/), [Google Gemini](https://ai.google.dev/), and [Streamlit](https://streamlit.io/). It can carry on human-like conversations, remember context, and even learn from uploaded PDF documents to assist you better.

## 🚀 Features

* 🤖 Powered by **Google Gemini 1.5 Pro**
* 📚 Upload PDF files to train the chatbot
* 🧠 Uses **LangChain Memory** to maintain conversation context
* 💬 Styled chat interface like WhatsApp/Instagram
* 🔒 Keeps responses short, human-like, and to the point

## 📦 Dependencies

Install the required Python libraries:

```bash
pip install streamlit langchain langchain-google-genai PyPDF2
```

> You will also need a [Google Generative AI API Key](https://ai.google.dev/) to use the chatbot.

## 📁 Project Structure

```
Garuda-Chatbot/
│
├── app.py              # Main Streamlit application
├── README.md           # Project README
└── requirements.txt    # Optional: Add dependencies here
```

## 🧠 How It Works

1. The app uses `LangChain`'s `LLMChain` to manage conversations.
2. Conversation history is maintained using `ConversationBufferMemory`.
3. You can upload one or more PDFs from the sidebar to "teach" the chatbot.
4. Responses are generated by **Gemini 1.5 Pro** using your API key.

## 🔑 Setting Up Your API Key

Update your API key in the code:

```python
model = ChatGoogleGenerativeAI(
    api_key="YOUR_GOOGLE_API_KEY", 
    model="gemini-1.5-pro"
)
```

> ⚠️ **Important:** Never expose your API key in public repositories. Use environment variables or a `.env` file for security.

## ▶️ Run the App

```bash
streamlit run app.py
```

## 🧪 Sample Usage

* Upload your study materials, resume, or manuals in PDF format.
* Start chatting with Garuda and ask questions like:

  * *"Summarize the uploaded PDF."*
  * *"What is the main topic discussed in the file?"*
  * *"Who wrote this document?"*

## 📸 Screenshot

![Screenshot 2025-05-06 010134](https://github.com/user-attachments/assets/75ecb84c-f5d4-4833-a6b5-bcebf5b96f00)

![Screenshot 2025-05-06 010209](https://github.com/user-attachments/assets/00167fc6-2c1b-4513-aabf-5796daac932e)
![Screenshot 2025-05-06 011047](https://github.com/user-attachments/assets/1e9b2939-1904-442f-9e0b-0b0e8a0a5fc4)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
