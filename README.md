# 🤖 AI Research Assistant

## 📌 Project Overview
The **AI Research Assistant** is a powerful, interactive web app designed to streamline online research by combining multiple AI models with web search and Wikipedia integration. Built with **Streamlit**, this app allows users to input queries and get structured, insightful responses — all within an intuitive, chat-style interface.

## 🎯 Features
- **Interactive Chat Interface:** Built using **Streamlit** for a smooth user experience.
- **Multi-AI Model Support:** Uses **LangChain** with **OpenAI** and **Anthropic** models for smart query processing.
- **Custom Research Tools:**
  - **Search Tool:** Integrates **DuckDuckGo** and **Wikipedia** for live web data.
  - **Wiki Tool:** Direct Wikipedia querying for fast knowledge retrieval.
  - **Save Tool:** Captures and stores research data for easy access.
- **Structured Response Parsing:** Parses output into topics, summaries, sources, and tools used.
- **Fallback Raw Output:** If parsing fails, the raw response is still presented for transparency.

## 🛠️ Tech Stack
- **Streamlit** — User-friendly web app interface
- **Python** — Core programming language
- **Dotenv** — Environment variable handling
- **Pydantic** — For structured response validation
- **LangChain** — Powering AI interactions via OpenAI and Anthropic
- **Azure Identity & OpenAI** — Cloud service integration

## 📁 Project Structure
```
📦 AI-Research-Assistant
│
├── 📄 app.py              # Streamlit UI setup
├── 📄 main.py             # Core AI logic and response handling
├── 📄 tools.py            # Custom research tools (DuckDuckGo, Wikipedia, Save)
└── 📄 requirements.txt    # Project dependencies
```

## 🚀 Setup and Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AI-Research-Assistant.git
   cd AI-Research-Assistant
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate    # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables:**
   Create a `.env` file and include your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```

5. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## 🧠 How It Works
- **User Input:** You type a research query in the chat interface.
- **Agent Processing:** The query is passed through `main.py`, where **LangChain** models (OpenAI/Anthropic) analyze it.
- **Tool Invocation:**
  - **DuckDuckGo** fetches live web data.
  - **Wikipedia** provides detailed knowledge.
  - **Save Tool** stores data.
- **Output Parsing:** Structured output (topic, summary, sources, tools) is presented — or raw output if parsing fails.

## 📌 Future Improvements
- ✅ Support for more AI models
- ✅ Enhanced error handling
- ✅ PDF export of research results
- ✅ Real-time analytics on queries

## 🎉 Contributions
Feel free to fork, improve, and submit pull requests. I’d love to see where this project can go with community input!

---

Made with ❤️ and AI by Syed Mohathashim Ali

#AI #MachineLearning #Streamlit #LangChain #OpenAI #Anthropic #Python #DataScience #ArtificialIntelligence

