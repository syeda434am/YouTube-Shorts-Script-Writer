import streamlit as st
from document_handler import create_txt_download_link, create_docx_download_link

def display_chat_sidebar():
    """Display the chat history sidebar."""
    with st.sidebar:
        # New Chat button
        if st.button("New Chat", key="new_chat_button", use_container_width=True):
            from chat_manager import create_new_chat
            create_new_chat()
        
        st.markdown("---")
        st.markdown("### Chat History")
        
        # Display chat history
        for chat_id, chat_data in sorted(
            st.session_state.chat_sessions.items(),
            key=lambda x: x[1]["created_at"],
            reverse=True
        ):
            # Highlight the current chat
            if chat_id == st.session_state.current_chat_id:
                button_style = "primary"
            else:
                button_style = "secondary"
            
            if st.button(
                f"{chat_data['title']} - {chat_data['created_at']}", 
                key=f"chat_{chat_id}", 
                use_container_width=True,
                type=button_style
            ):
                from chat_manager import select_chat
                select_chat(chat_id)

def display_chat_messages(current_chat):
    """Display the chat messages for the current conversation."""
    chat_container = st.container()
    with chat_container:
        # Display all messages except system messages
        for message in [m for m in current_chat["messages"] if m["role"] != "system"]:
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:  # assistant
                st.markdown(f"**AI:**")
                st.markdown(message["content"])
                st.markdown("---")

def display_download_options(script_text, title):
    """Display download options for the finalized script."""
    st.markdown("### Download Options")
    
    col1, col2 = st.columns(2)
    
    # Clean the filename
    clean_title = title.replace("...", "").replace(" ", "_")
    if not clean_title:
        clean_title = "script"
    
    with col1:
        filename = f"{clean_title}.txt"
        st.markdown(create_txt_download_link(script_text, filename), unsafe_allow_html=True)
    
    with col2:
        filename = f"{clean_title}.docx"
        st.markdown(create_docx_download_link(script_text, filename), unsafe_allow_html=True)

def display_chat_input():
    """Display the chat input form."""
    with st.form(key="chat_input_form", clear_on_submit=True):
        user_input = st.text_area("Your message:", height=100, key="user_input")
        submit_button = st.form_submit_button("Send", use_container_width=True)
    
    return user_input if submit_button else None