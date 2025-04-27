# 🍔 Zomato Gen AI – Food Assistant Chatbot

An end-to-end GenAI-powered chatbot system for Zomato.  
It scrapes restaurant data, builds a FAISS-based knowledge base, and provides a Streamlit web interface to answer user queries using both retrieved information and a large language model (LLM).

---
## Overview
This project implements a Generative AI solution combining web scraping with a Retrieval Augmented Generation (RAG) chatbot to enhance user experience on Zomato.

## Components
1. **Web Scraper**: Scrapes restaurant data from specified websites.
2. **Knowledge Base**: Processes and stores the scraped data.
3. **RAG-based Chatbot**: Answers user queries about restaurants.
4. **User Interface**: A Streamlit app for user interaction.


## 📂 Project Structure

```bash
zomato_gen_ai/
│
├── scraper/                # Scrapes restaurant data
│   ├── scraper.py
│   └── requirements.txt
│
├── knowledge_base/         # Builds FAISS vectorstore from scraped data
│   ├── create_kb.py
│   └── requirements.txt
│
├── chatbot/                # Retrieval + generation logic
│   ├── chatbot.py
│   └── requirements.txt
│
├── interface/              # Streamlit frontend
│   ├── app.py
│   └── requirements.txt
│
├── data/                   # Raw and processed data
│   └── restaurant_data.json
│
├── README.md               # This documentation
└── requirements.txt        # Combined root dependencies
```

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/zomato_gen_ai.git
cd zomato_gen_ai
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
# macOS/Linux:
source venv/bin/activate
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install **all at once**:

```bash
pip install -r requirements.txt
```

_or_ module-by-module:

```bash
pip install -r scraper/requirements.txt
pip install -r knowledge_base/requirements.txt
pip install -r chatbot/requirements.txt
pip install -r interface/requirements.txt
```

### 4. Configure Hugging Face Token

```bash
# Linux / macOS
export HF_TOKEN="your_huggingface_api_token"

# Windows CMD
set HF_TOKEN="your_huggingface_api_token"

# Windows PowerShell
$env:HF_TOKEN="your_huggingface_api_token"
```
---
## 📈 Usage Guide

1. **Scrape Data**  
   ```bash
   cd scraper
   python scraper\scraper.py
   ```  
   Produces `data/restaurant_data.json`

2. **Build Knowledge Base**  
   ```bash
   cd knowledge_base
   python knowledge_base\create_kb.py
   ```  
   Generates a FAISS vectorstore under `knowledge_base/vectorstore/`

3. **Run Chatbot Interface**  
   ```bash
   cd interface
   streamlit run interface\app.py
   ```  
   Opens the Streamlit app in your browser

4. **Chat!**  
   Ask about restaurants, cuisines, menus, or general food questions.  
   The system will retrieve relevant snippets from the JSON/PDF knowledge base; if none match, it falls back on the LLM.

---
## ⚙️ Tech Stack

| Component        | Technology                             |
| :--------------- | :--------------------------------------|
| **Scraper**      | Python, `requests`, `beautifulsoup4`   |
| **Embeddings**   | `sentence-transformers/all-MiniLM-L6-v2` |
| **Vector Store** | FAISS (`faiss-cpu`)                    |
| **LLM**          | Mistral-7B Instruct via HuggingFace Hub|
| **Frontend**     | Streamlit                              |
| **Data Storage** | JSON                                   |

---

## 📚 Root Requirements (`requirements.txt`)

```
streamlit
requests
beautifulsoup4
langchain
sentence-transformers
faiss-cpu
huggingface_hub
langchain-community
langchain-huggingface
```

*Each sub-folder also has its own `requirements.txt` if you prefer isolated installs.*

---

## 🎯 Example Workflow

1. **scraper/** → gathers raw restaurant info  
2. **knowledge_base/** → embeds and indexes data  
3. **interface/** → serves the chat UI  
4. **chatbot/** → handles retrieval & generation  

---

## 📢 Customization & Notes

- **Model**: Swap out `mistralai/Mistral-7B-Instruct-v0.3` in any config.  
- **Retrieval**: Adjust `k` (number of docs) via sidebar slider.  
- **Prompts**: Tweak templates in `chatbot.py` for different behavior.  
- **Lightweight Option**: Use smaller LLMs or reduce `max_new_tokens` for faster response.

---

## 📜 License

This project is released under the **MIT License**.  
Feel free to use, modify, and share!

---

# ✨ Happy Chatting with Zomato Gen AI!
