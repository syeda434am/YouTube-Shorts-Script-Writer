# YouTube-Shorts-Script_Writer
A powerful AI-powered application for generating and exporting YouTube short-video scripts.

## Overview

Tube ScriptWriter is a Streamlit-based web application that helps content creators generate video scripts quickly and efficiently using AI. The application allows you to:

- Generate script outlines and drafts using AI
- Edit and refine scripts in a user-friendly interface
- Export scripts as text or Word documents
- Manage multiple script versions in chat-like sessions

## Project Structure

```
YouTube-Shorts-Script-Writer/
├── .env                  # API key storage
├── app.py                # Main application file
├── ai_generator.py       # AI response generation module
├── document_handler.py   # Document creation and download functions
├── chat_manager.py       # Chat session management
├── ui_components.py      # UI display components
└── requirements.txt      # Project dependencies
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/syeda434am/YouTube-Shorts-Script-Writer.git
   cd YouTube-Shorts-Script-Writer
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   # or 
   GROQ_API_KEY=your_api_key_here
   ```

## Running the Application

Start the application by running:

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501` in your web browser.

## Usage

1. **Start a New Script**:
   - Enter a topic or title for your video
   - Specify your target audience, length, and style preferences
   - Click "Generate Script" to create an initial draft

2. **Edit Your Script**:
   - Use the text editor to refine the generated script
   - Add comments or instructions for AI refinements
   - Request specific improvements or changes

3. **Export Your Script**:
   - Download your finished script as a .txt or .docx file
   - Save different versions for future reference

4. **Manage Sessions**:
   - Create multiple script projects
   - Switch between different script sessions
   - Continue working on previous drafts

## Configuration Options

You can customize the AI behavior in `ai_generator.py` by modifying the prompt templates and model parameters to better match your content creation style and needs.

## Dependencies

- streamlit: Web application framework
- openai / anthropic: AI API integrations
- python-docx: Word document generation
- python-dotenv: Environment variable management
- pandas: Data handling

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.