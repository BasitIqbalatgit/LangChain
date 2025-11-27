# Indexing Consist of Following part:
# 1. Document Loader
# 2. TextSpliter
# 3. Vector Store

# Lets Start Doing all of these


# ------------------------------------------------------Document Loader---------------------------------------
# url -> extract_video_id -> id -> get_Transcript -> transcript
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS

import re

def extract_video_id(url):
    """
    Extracts the YouTube video ID from a URL.
    
    Args:
        url (str): The YouTube video URL.
        
    Returns:
        str: The video ID extracted from the URL or None if no valid ID found.
    """
    video_id_regex = r'(?:https?://)?(?:www\.)?(?:youtube\.com(?:/[^/]+)*\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    
    match = re.search(video_id_regex, url)
    
    if match:
        return match.group(1)
    return None

# Get transcript for the given video ID, checking multiple languages
def get_transcript_from_video_id(video_id):
    try:
        yt_transcript_api = YouTubeTranscriptApi()

        # First try English, then fall back to other languages if necessary
        available_languages = ['en-US', 'en', 'hi', 'ar', 'zh-Hant', 'nl', 'fr', 'de', 'id', 'it', 'ja', 'ko', 'pt', 'ru', 'es', 'th', 'tr', 'uk', 'vi']
        
        # Try each language in the list until one succeeds
        for lang in available_languages:
            try:
                print(f"Trying to fetch transcript in {lang}...")
                transcript = yt_transcript_api.fetch(video_id, languages=[lang])
                if transcript:
                    print(f"Found transcript in {lang}.")
                    break  # Exit loop if transcript is found
            except Exception as e:
                print(f"Transcript not found in {lang}. Trying next language...")

        # If transcript is found, format it; else return None
        if transcript:
            formatter = TextFormatter()
            formatted_transcript = formatter.format_transcript(transcript)
            return formatted_transcript

        print("No transcript found in any of the available languages.")
        return None

    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

#----------------------------------------------------------Text Splitter----------------------------------
# transcript -> split_transcript -> docs(List [ Document ])

load_dotenv()
def split_transcript_to_Doc(transcript):
    semantic_text_splitter = SemanticChunker(
        OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
    )

    
    docs = semantic_text_splitter.create_documents([transcript])
    print("\n\n\nLength of Doc is :",len(docs))
    return docs

#------------------------------------------------------------Storing in VectorStores----------------
# docs -> store in FAISS -> stored Successfully

def store_docs_in_FAISS(docs, save_path="faiss_index"):
    """
    Store documents in FAISS vector store and save to disk.
    
    Args:
        docs: List of documents to store
        save_path: Path where the FAISS index will be saved
    
    Returns:
        str: The path where the index was saved
    """
    vector_store = FAISS.from_documents(
        documents=docs,
        embedding=OpenAIEmbeddings()
    )
    
    # Save the FAISS index to disk
    vector_store.save_local(save_path)
    print(f"FAISS index saved successfully at: {save_path}")
    
    return save_path
