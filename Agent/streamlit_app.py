import streamlit as st
from langchain.agents import create_agent
from researcher import research
from summarizer import summarize
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stChatMessage {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    .tool-call {
        background-color: #e8f4f8;
        border-left: 4px solid #1f77b4;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .success-box {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize the orchestrator agent
@st.cache_resource
def initialize_agent():
    """Initialize the orchestrator agent"""
    return create_agent(
        model='gpt-4o-mini',
        tools=[research, summarize],
        system_prompt=(
            "You are a supervisor agent. "
            "When the user gives a request, you decide whether to first call research_topic (to gather data), "
            "and then call summarize_text (to produce final answer). "
            "Return the final output to the user. "
            "You may call both tools in sequence when needed."
        )
    )

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'processing' not in st.session_state:
    st.session_state.processing = False

# Header
st.markdown('<div class="main-header">🤖 AI Research Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Ask me anything and I\'ll research and summarize the information for you!</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This AI Research Assistant uses:
    - **Research Agent**: Searches the web for relevant information
    - **Summarizer Agent**: Creates concise summaries
    - **Orchestrator**: Coordinates the workflow
    
    ### How it works:
    1. You ask a question
    2. The agent researches the topic online
    3. Gathers information from multiple sources
    4. Summarizes the findings
    5. Presents a clear, concise answer
    """)
    
    st.divider()
    
    st.header("⚙️ Settings")
    show_tool_calls = st.checkbox("Show agent thinking process", value=True)
    
    st.divider()
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    st.markdown("### 💡 Example Questions")
    example_questions = [
        "What are the latest developments in quantum computing?",
        "Explain artificial intelligence in simple terms",
        "What is the current state of renewable energy?",
        "Tell me about recent breakthroughs in medicine"
    ]
    
    for question in example_questions:
        if st.button(question, key=f"example_{question}", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": question})
            st.rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Display tool calls if available and enabled
        if show_tool_calls and "tool_calls" in message and message["tool_calls"]:
            with st.expander("🔧 View Agent Thinking Process"):
                for tool_call in message["tool_calls"]:
                    st.markdown(f"**Tool Used:** `{tool_call['tool']}`")
                    if 'status' in tool_call:
                        st.markdown(f"**Status:** {tool_call['status']}")

# Chat input
if prompt := st.chat_input("What would you like to learn about?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with streaming effect
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        status_placeholder = st.empty()
        
        try:
            # Show processing status
            with status_placeholder.container():
                with st.status("Processing your request...", expanded=True) as status:
                    st.write("🔍 Analyzing your question...")
                    time.sleep(0.5)
                    
                    st.write("🌐 Researching the topic...")
                    
                    # Initialize and invoke the orchestrator
                    orchestrator = initialize_agent()
                    
                    response = orchestrator.invoke({
                        'messages': [
                            {'role': 'user', 'content': prompt}
                        ]
                    })
                    
                    st.write("✅ Research complete!")
                    st.write("📝 Generating summary...")
                    time.sleep(0.5)
                    
                    status.update(label="Complete!", state="complete", expanded=False)
            
            # Extract the final response
            final_response = response['messages'][-1].content
            
            # Display the response
            message_placeholder.markdown(final_response)
            
            # Store assistant response with metadata
            assistant_message = {
                "role": "assistant",
                "content": final_response
            }
            
            # Extract tool calls if show_tool_calls is enabled
            if show_tool_calls:
                tool_calls = []
                # Check if there are intermediate messages indicating tool usage
                for msg in response['messages'][:-1]:
                    if hasattr(msg, 'additional_kwargs') and 'tool_calls' in msg.additional_kwargs:
                        for tc in msg.additional_kwargs['tool_calls']:
                            tool_calls.append({
                                'tool': tc.get('function', {}).get('name', 'unknown'),
                                'status': 'executed'
                            })
                
                if tool_calls:
                    assistant_message["tool_calls"] = tool_calls
            
            st.session_state.messages.append(assistant_message)
            
        except Exception as e:
            error_message = f"❌ An error occurred: {str(e)}"
            message_placeholder.error(error_message)
            st.session_state.messages.append({
                "role": "assistant",
                "content": error_message
            })

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9rem;'>
    <p>Powered by LangChain & OpenAI GPT-4 | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
