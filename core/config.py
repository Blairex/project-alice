import os
from dotenv import load_dotenv

load_dotenv()

WAKE_WORD = os.getenv("WAKE_WORD", "alice")
OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
