from pydantic import BaseModel


class EmailPrompt(BaseModel):
    email_prompt: str

    class Config:
        schema_extra = {"example": {"email_prompt": "Sky is Blue"}}


class EmailResponse(BaseModel):
    email_content: str
