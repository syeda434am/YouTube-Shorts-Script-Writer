import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Get API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# System prompt for Zack D. Films style YouTube Shorts scriptwriting
SYSTEM_PROMPT = """
You are an expert scriptwriter for YouTube Shorts in the style of Zack D. Films. 
Generate a short, engaging script of 100-150 words based on the user's topic. 
The tone should be conversational, punchy, and story-driven with:
- Sensational, curiosity-driven hooks
- Concise, authoritative narration in past tense, third person
- Vivid, graphic imagery delivered matter-of-factly
- Suspenseful pacing with information dripped out in rapid, measured steps
- No personal commentary or humor; maintain a detached, documentary-style voice

Output the script as plain text, ready for voiceover.
"""

def get_groq_response(messages):
    """Generate a response from the Groq API based on chat messages."""
    try:
        # Initialize Groq Chat model
        groq_chat = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="meta-llama/llama-4-scout-17b-16e-instruct"
        )
        
        # Format messages for the LangChain ChatGroq API
        formatted_messages = []
        
        # Always add the system message first
        formatted_messages.append({"role": "system", "content": SYSTEM_PROMPT})
        
        # Add all user and assistant messages
        for msg in messages:
            if msg["role"] != "system":  # Skip system messages as we already added our own
                formatted_messages.append(msg)
        
        # Get response from Groq
        response = groq_chat.invoke(formatted_messages)
        
        # Extract content from the response
        if hasattr(response, 'content'):
            content = response.content
        else:
            content = str(response)
            
        return content
    except Exception as e:
        return f"Error generating response: {str(e)}"