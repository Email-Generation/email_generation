import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    OPENAI_ORGANIZATION: str = os.getenv("OPENAI_ORGANIZATION")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    title: str = "Email Generation API"
    description: str = (
        "A powerful API for generating customized email content using the GPT-3.5 language model. Create compelling"
        " email responses effortlessly by providing prompts, and receive intelligently generated content. Streamline"
        " your communication with the Email Generation API."
    )

    # Project Settings
    APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR = os.path.dirname(APP_DIR)

    DEFAULT_LOGGING_CONFIG_DIR = os.path.join(APP_DIR, "config", "logging")

    class Config:
        env_file = ".env"


# Load settings from the .env file
settings = Settings()
