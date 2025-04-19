import uuid
from datetime import datetime
import streamlit as st
from ai_generator import SYSTEM_PROMPT

def initialize_session_state():
    """Initialize the session state for chat management."""
    # Initialize chat sessions dictionary if it doesn't exist
    if "chat_sessions" not in st.session_state:
        st.session_state.chat_sessions = {}
    
    # Initialize current chat ID if it doesn't exist
    if "current_chat_id" not in st.session_state:
        new_chat_id = str(uuid.uuid4())
        st.session_state.current_chat_id = new_chat_id
        st.session_state.chat_sessions[new_chat_id] = {
            "title": "New Chat",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT}
            ],
            "finalized_script": None
        }

def create_new_chat():
    """Create a new chat session."""
    new_chat_id = str(uuid.uuid4())
    st.session_state.current_chat_id = new_chat_id
    st.session_state.chat_sessions[new_chat_id] = {
        "title": "New Chat",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT}
        ],
        "finalized_script": None
    }
    st.rerun()

def select_chat(chat_id):
    """Select an existing chat session."""
    st.session_state.current_chat_id = chat_id
    st.rerun()

def update_chat_title(chat_id, first_message):
    """Update the chat title based on the first user message."""
    # Use the first few words of the first message as the chat title
    words = first_message.split()
    title = " ".join(words[:4]) + ("..." if len(words) > 4 else "")
    st.session_state.chat_sessions[chat_id]["title"] = title

def finalize_script(chat_id, script_text):
    """Mark a script as finalized in the current chat session."""
    st.session_state.chat_sessions[chat_id]["finalized_script"] = script_text

def get_current_chat():
    """Get the current chat session data."""
    return st.session_state.chat_sessions[st.session_state.current_chat_id]