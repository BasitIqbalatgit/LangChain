import streamlit as st
from Indexing import get_transcript_from_video_id, extract_video_id, split_transcript_to_Doc, store_docs_in_FAISS
from Retriver import MMRRetriever
from Generation import generate_response
import os

# Streamlit App
st.title("YouTube Transcript Chatbot")

# Step 1: Input YouTube URL to extract transcript
if 'transcript' not in st.session_state:
    st.session_state.transcript = None  # Initialize empty transcript

# Input field for URL
if st.session_state.transcript is None:
    st.header("Enter YouTube Video URL")

    # URL Input
    url = st.text_input("Enter YouTube URL:")

    if st.button("Load Transcript") and url:
        with st.spinner("Loading transcript and building index..."):
            # Extract video ID and fetch transcript
            video_id = extract_video_id(url)
            if video_id:
                transcript = get_transcript_from_video_id(video_id)
                if transcript:
                    st.session_state.transcript = transcript
                    st.session_state.video_url = url
                    
                    # Split transcript into documents
                    docs = split_transcript_to_Doc(transcript)
                    
                    # Store documents in FAISS and save the index
                    index_path = os.path.join("RAG", "Project", f"faiss_index_{video_id}")
                    store_docs_in_FAISS(docs, save_path=index_path)
                    st.session_state.faiss_index_path = index_path
                    
                    st.success("Transcript loaded and indexed successfully! Redirecting to chat...")
                    st.rerun()
                else:
                    st.error("Failed to fetch transcript.")
            else:
                st.error("Invalid YouTube URL.")
    
    elif not url:
        st.warning("Please enter a valid YouTube URL to proceed.")

# Step 2: If transcript is loaded, show chat interface
else:
    st.header("Chat with YouTube Video Transcript")
    
    # Display video preview
    st.video(st.session_state.video_url)
    st.caption(f"Video URL: {st.session_state.video_url}")
    st.divider()

    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for i, chat in enumerate(st.session_state.chat_history):
        with st.chat_message("user"):
            st.write(chat["question"])
        with st.chat_message("assistant"):
            st.write(chat["answer"])

    # Chatbot-like interface
    user_query = st.chat_input("Ask a question about the video:")

    if user_query:
        # Display user message
        with st.chat_message("user"):
            st.write(user_query)
        
        # Generate response using RAG chain
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Create retriever and generate response using the chain
                    retriever = MMRRetriever(faiss_index_path=st.session_state.faiss_index_path)
                    response = generate_response(retriever, user_query)
                    st.write(response)
                    
                    # Add to chat history
                    st.session_state.chat_history.append({
                        "question": user_query,
                        "answer": response
                    })
                except Exception as e:
                    st.error(f"Error generating response: {str(e)}")
                    st.write("Please try rephrasing your question.")

    # Sidebar options
    with st.sidebar:
        st.header("Options")
        if st.button("Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
        
        if st.button("Load New Video"):
            st.session_state.transcript = None
            st.session_state.chat_history = []
            st.rerun()
