<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&lines=Converso+AI+🤖;Your+Intelligent+Chat+Companion;Powered+by+Amazon+Nova+Pro" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![AWS](https://img.shields.io/badge/AWS_Bedrock-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

<p align="center">
  <i>A sleek, memory-powered AI chatbot built with Streamlit, LangChain, and Amazon Bedrock's Nova Pro model</i>
</p>

---

</div>

## 🖼️ Preview

<div align="center">
  <img src="chatbot.png" alt="Converso AI Chatbot Preview" width="85%" style="border-radius: 12px;" />
</div>

---

## ✨ Features

- 🧠 **Persistent Memory** — Remembers the full conversation using LangChain message history
- ⚡ **Powered by Amazon Nova Pro** — Fast, accurate responses via AWS Bedrock
- 💬 **Clean Chat UI** — Simple and elegant Streamlit interface
- 🔄 **Real-time Responses** — Dynamic multi-turn conversation support
- 🔒 **AWS Credentials Integration** — Secure access via `~/.aws/credentials`

---

## 🗂️ Project Structure

```
converso-ai/
│
├── chatbot_frontend.py          # 🖥️  Streamlit UI & session state
├── chatbot_backend.py           # 🧠  Memory + conversation logic
└── chatbot_backend_intermediate.py  # 🔧  Standalone LLM test
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/converso-ai.git
cd converso-ai
```

### 2. Install Dependencies

```bash
pip install streamlit langchain-aws langchain-core boto3
```

### 3. Configure AWS Credentials

Make sure your AWS credentials are set up with Bedrock access:

```bash
aws configure
```

Or edit `~/.aws/credentials`:

```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region = us-east-1
```

> ⚠️ Ensure your IAM user/role has access to **Amazon Bedrock** and the **Nova Pro** model in `us-east-1`.

### 4. Run the App

```bash
streamlit run chatbot_frontend.py
```

---

## 🧩 How It Works

```
User Input
    │
    ▼
chatbot_frontend.py          ← Captures input, manages session state
    │
    ▼
chatbot_backend.py           ← Builds message history + calls LLM
    │
    ▼
LangChain + AWS Bedrock      ← Amazon Nova Pro processes the conversation
    │
    ▼
Response displayed in UI     ← Chat history updated with AI reply
```

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Streamlit |
| **Backend** | Python + LangChain |
| **LLM Model** | Amazon Nova Pro (`us.amazon.nova-pro-v1:0`) |
| **Cloud** | AWS Bedrock (us-east-1) |
| **Memory** | LangChain `HumanMessage` / `AIMessage` |

---

## 📁 File Breakdown

### `chatbot_frontend.py`
> Streamlit UI that initializes memory once per session, captures user input, calls the backend, and renders the full chat history.

### `chatbot_backend.py`
> Production-ready backend. Initializes the LLM, manages a global chat history list, and handles multi-turn conversation with memory.

### `chatbot_backend_intermediate.py`
> Standalone test script to verify Bedrock connectivity. Sends a single message and prints the model's response — great for debugging.

---

## 🌱 Future Improvements

- [ ] 🎨 Custom CSS for a more polished UI
- [ ] 📄 PDF/document upload & Q&A
- [ ] 🌐 Multi-language support
- [ ] 💾 Persistent chat history (database integration)
- [ ] 🔑 API key support as alternative to AWS credentials

---

<div align="center">

Made by **Akanksha**

</div>
