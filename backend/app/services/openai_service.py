import openai
from app.config.settings import settings
from fastapi import HTTPException, status
from openai import ChatCompletion

from app.config.logging import get_logger


logger = get_logger()

openai.organization = settings.OPENAI_ORGANIZATION
openai.api_key = settings.OPENAI_API_KEY


def generate_email(email_prompt: str) -> str:
    try:
        req = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": email_prompt}],
        )

        if req:
            email_output = req.choices[0].message.content
            # email_split = email_output.split("\n")
            # for i in range(len(email_split)):
            #     email_split[i] = "<p>" + email_split[i] + "</p>"
            # email_output = "".join(email_split)
            return email_output
        else:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Invalid Request",
            )
    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Out of service"
        )
