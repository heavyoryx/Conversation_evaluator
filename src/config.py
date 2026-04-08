import os

from dotenv import load_dotenv


load_dotenv()


def get_openai_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")
    return api_key


OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4")
