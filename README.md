# MULTI-AI-AGENT

A modular, multi-agent AI system with a FastAPI backend and a Streamlit frontend. This project demonstrates how to orchestrate multiple AI agents and tools for advanced conversational and search capabilities.

## Features
- **FastAPI Backend**: Handles chat requests and orchestrates AI agents.
- **Streamlit Frontend**: User-friendly web interface for interacting with the agents.
- **LangChain Integration**: Utilizes LangChain for agent logic and tool use.
- **Pluggable Tools**: Easily add or remove tools (e.g., search) for the agents.
- **Custom Exception Handling & Logging**: Robust error handling and logging for easier debugging.

## Prerequisites
- Python 3.12+
- [pip](https://pip.pypa.io/en/stable/)
- (Recommended) [virtualenv](https://virtualenv.pypa.io/en/latest/)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/MULTI-AI-AGENT.git
   cd MULTI-AI-AGENT
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables
- Copy `.env.example` to `.env` and fill in the required API keys (e.g., for Groq, or any other services you use).
- Example:
  ```env
  GROQ_API_KEY=your_groq_api_key
  TAVILY_API_KEY=your_tavily_api_key
  # Add other keys as needed
  ```

## Running the Application

### 1. Start Backend and Frontend Together
The main entry point will start both services:
```bash
python app/main.py
```
- Backend (FastAPI): [http://127.0.0.1:9999](http://127.0.0.1:9999)
- Frontend (Streamlit): [http://localhost:8501](http://localhost:8501)

### 2. Run Backend Only
```bash
uvicorn app.backend.api:app --host 127.0.0.1 --port 9999
```

### 3. Run Frontend Only
```bash
streamlit run app/frontend/ui.py
```

## Project Structure
```
app/
  backend/      # FastAPI backend
  frontend/     # Streamlit frontend
  core/         # AI agent logic
  common/       # Logging and custom exceptions
  config/       # Settings and environment config
  main.py       # Entry point to run both backend and frontend
logs/           # Log files
requirements.txt
setup.py
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE) 