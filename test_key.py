import os
from dotenv import load_dotenv

load_dotenv()

print("API KEY FOUND:", os.getenv("OPENAI_API_KEY") is not None)
