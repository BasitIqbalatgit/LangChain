# 🎥 YouTube Transcript Chatbot

A powerful RAG (Retrieval-Augmented Generation) chatbot that lets you chat with YouTube video transcripts using AI.

## ✨ Features

- 🎬 **YouTube Integration**: Paste any YouTube URL to chat with the video
- 🎥 **Video Preview**: Watch the video while asking questions
- 🧠 **Smart Retrieval**: Uses FAISS + MMR for intelligent document retrieval
- 🤖 **AI-Powered**: Powered by OpenAI GPT-3.5 with LangChain
- 💬 **Chat History**: Persistent conversation context
- 🌐 **Multi-Language**: Supports transcripts in multiple languages

## 🏗️ Architecture

```
YouTube URL → Transcript Extraction → Semantic Chunking → 
FAISS Vector Store → MMR Retrieval → Prompt + Context → 
GPT-3.5 → Answer
```

### Components:
1. **Indexing.py**: YouTube transcript fetching and document processing
2. **Retriver.py**: MMR-based vector search with FAISS
3. **Augmentation.py**: Prompt template and context formatting
4. **Generation.py**: LangChain LCEL pipeline for response generation
5. **main.py**: Streamlit UI with chat interface

## 🚀 Quick Start (Local)

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment**:
   ```bash
   cp .env.example .env
   # Add your OpenAI API key to .env
   ```

3. **Run the app**:
   ```bash
   streamlit run main.py
   ```

4. **Open browser**: http://localhost:8501

## 🌐 Get Public URL (Deploy to Streamlit Cloud)

### Quick Steps:

1. **Push to GitHub**:
   ```bash
   git add RAG/Project/
   git commit -m "Add YouTube Chatbot"
   git push origin main
   ```

2. **Deploy**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select repository and set **Main file path**: `RAG/Project/main.py`
   - Add your `OPENAI_API_KEY` in secrets
   - Click "Deploy"

3. **Get your URL**: 
   ```
   https://your-app-name.streamlit.app
   ```

📖 **[See detailed deployment guide →](DEPLOYMENT.md)**

## 📦 Requirements

- Python 3.8+
- OpenAI API key
- Internet connection (for YouTube and OpenAI API)

## 💡 Usage

1. Enter a YouTube URL
2. Wait for transcript indexing (30 seconds - 2 minutes)
3. Ask questions about the video
4. Get AI-generated answers based on the transcript

## 🔧 Configuration

### Model Settings (in Generation.py):
- **Model**: GPT-3.5-turbo
- **Temperature**: 0 (deterministic)
- **MMR Lambda**: 0.5 (balance relevance/diversity)

### Retrieval Settings (in Retriver.py):
- **Top K**: 5 documents
- **Fetch K**: 20 candidates for MMR

## 🎯 Use Cases

- 📚 Educational content Q&A
- 🎓 Lecture note-taking
- 📺 Video research
- 🗣️ Interview analysis
- 📝 Content summarization

## 🔐 Security

- API keys stored in environment variables
- Never commit `.env` file
- Use Streamlit Cloud secrets for deployment

## 📊 Cost Estimate

Per video (~10 min):
- **Transcript**: Free
- **Embeddings**: ~$0.01
- **Queries (10)**: ~$0.01
- **Total**: ~$0.02 per video

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Cloud storage for FAISS indices
- Video metadata display
- Playlist support
- Export chat history
- Custom embeddings models

## 📝 License

MIT License - feel free to use and modify!

## 🆘 Support

- Issues: GitHub Issues
- Streamlit: [docs.streamlit.io](https://docs.streamlit.io)
- LangChain: [python.langchain.com](https://python.langchain.com)

---

**Built with**: LangChain, Streamlit, OpenAI, FAISS
