from pydantic import BaseSettings


class Settings(BaseSettings):
    OPENAI_ORGANIZATION: str
    OPENAI_API_KEY: str

    title: str = "Email Generation API"
    description: str = (
        "A powerful API for generating customized email content using the GPT-3.5"
        " language model. Create compelling email responses effortlessly by providing"
        " prompts, and receive intelligently generated content. Streamline your"
        " communication with the Email Generation API."
    )

    class Config:
        env_file = ".env"
