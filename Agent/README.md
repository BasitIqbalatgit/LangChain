# AI Research Assistant - Streamlit UI

A powerful AI-powered research assistant that searches the web, gathers information, and provides concise summaries using LangChain agents.

## Features

- 🤖 **Intelligent Agent Orchestration**: Supervisor agent coordinates research and summarization
- 🔍 **Web Research**: Automatically searches and extracts information from multiple sources
- 📝 **Smart Summarization**: Generates clear, concise summaries of research findings
- 💬 **Chat Interface**: Interactive chat-based UI for natural conversations
- 🎨 **Modern Design**: Clean, responsive interface with custom styling
- 🔧 **Transparency**: Optional view of agent thinking process and tool usage

## Architecture

The application uses three main agents:

1. **Orchestrator Agent** (`main.py`): Supervises the workflow and decides which tools to call
2. **Research Agent** (`researcher.py`): Searches the web and loads content from pages
3. **Summarizer Agent** (`summarizer.py`): Creates concise summaries from raw text

## Prerequisites

- Python 3.12+
- OpenAI API key

## Installation

1. **Install dependencies**:
```bash
cd Agent
pip install -r requirements.txt
```

2. **Set up environment variables**:
Create a `.env` file in the `Agent` directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

### Streamlit UI (Recommended)

Run the Streamlit web interface:
```bash
streamlit run streamlit_app.py
```

The app will open automatically in your default browser at `http://localhost:8501`

### Command Line Interface

Alternatively, run the CLI version:
```bash
python main.py
```

## Usage

1. **Start the application** using one of the methods above
2. **Enter your question** in the chat input (e.g., "What are the latest developments in quantum computing?")
3. **Wait for the agent** to research and summarize the information
4. **View the results** in the chat interface

### Features in Streamlit UI

- **Example Questions**: Click on pre-made questions in the sidebar
- **Agent Thinking Process**: Toggle to see which tools the agent uses
- **Clear Chat**: Reset conversation history with one click
- **Responsive Design**: Works on desktop and mobile devices

## Example Questions

- "What are the latest developments in quantum computing?"
- "Explain artificial intelligence in simple terms"
- "What is the current state of renewable energy?"
- "Tell me about recent breakthroughs in medicine"

## Project Structure

```
Agent/
├── streamlit_app.py      # Streamlit web interface
├── main.py               # CLI version
├── researcher.py         # Research agent with web tools
├── summarizer.py         # Summarization agent
├── tools.py              # Custom tools (web search, page loader)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API keys)
└── README.md            # This file
```

## Troubleshooting

### API Key Issues
- Ensure your `.env` file is in the `Agent` directory
- Verify your OpenAI API key is valid and has credits

### Import Errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're in the correct directory when running commands

### Streamlit Not Found
```bash
pip install streamlit
```

### Port Already in Use
If port 8501 is already in use, specify a different port:
```bash
streamlit run streamlit_app.py --server.port 8502
```

## Technologies Used

- **LangChain**: Framework for building LLM applications
- **OpenAI GPT-4**: Language model for intelligent responses
- **Streamlit**: Web framework for the UI
- **DuckDuckGo Search**: Web search functionality
- **Python**: Core programming language

## License

This project is part of the LangChain learning repository.

## Contributing

Feel free to submit issues and enhancement requests!
