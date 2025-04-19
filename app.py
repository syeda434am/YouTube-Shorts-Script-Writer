import streamlit as st
from chat_manager import initialize_session_state, get_current_chat, update_chat_title, finalize_script
from ui_components import display_chat_sidebar, display_chat_messages, display_download_options, display_chat_input
from ai_generator import get_groq_response

def main():
    """Main application function."""
    st.set_page_config(page_title="Youtube Shorts Script Generator", layout="wide")
    
    # Initialize session state
    initialize_session_state()
    
    # Display sidebar with chat history
    display_chat_sidebar()
    
    # Get current chat data
    current_chat = get_current_chat()
    
    # Display header
    st.title("YouTube Shorts Script Generator")
    st.markdown(
        """
        Chat with the AI to generate YouTube Shorts scripts in the style of Zack D. Films. 
        Once you're satisfied with the script, finalize it and download in your preferred format.
        """
    )
    
    # Check if there's a finalized script already
    if current_chat.get("finalized_script"):
        st.success("Script has been finalized! You can download it below.")
        
        # Display the finalized script
        st.markdown("### Finalized Script")
        st.text_area("Script", value=current_chat["finalized_script"], height=200, disabled=True)
        
        # Display download options
        display_download_options(current_chat["finalized_script"], current_chat["title"])
        
        # Option to continue editing
        if st.button("Create New Script", key="new_script"):
            current_chat["finalized_script"] = None
            st.rerun()
    else:
        # Display chat messages
        display_chat_messages(current_chat)
        
        # Option to finalize the current script
        if len([m for m in current_chat["messages"] if m["role"] == "assistant"]) > 0:
            # Get the last assistant message
            last_assistant_message = [m for m in current_chat["messages"] if m["role"] == "assistant"][-1]
            
            # Finalize button
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("Finalize Script", key="finalize", use_container_width=True):
                    finalize_script(st.session_state.current_chat_id, last_assistant_message["content"])
                    st.rerun()
        
        # Input form at the bottom
        st.markdown("---")
        user_input = display_chat_input()
        
        if user_input and user_input.strip():
            # Add user message to the current chat
            current_chat["messages"].append({"role": "user", "content": user_input})
            
            # Update chat title if this is the first user message
            if len([m for m in current_chat["messages"] if m["role"] == "user"]) == 1:
                update_chat_title(st.session_state.current_chat_id, user_input)
            
            # Get AI response
            with st.spinner("Thinking..."):
                ai_response = get_groq_response(current_chat["messages"])
            
            # Add AI response to the conversation
            current_chat["messages"].append({"role": "assistant", "content": ai_response})
            
            # Refresh the page to display the new messages
            st.rerun()

if __name__ == "__main__":
    main()