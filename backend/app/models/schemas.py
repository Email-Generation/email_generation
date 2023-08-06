from pydantic import BaseModel


class EmailPrompt(BaseModel):
    email_prompt: str


class EmailResponse(BaseModel):
    email_content: str
