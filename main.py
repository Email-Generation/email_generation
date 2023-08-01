from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import openai
from mangum import Mangum

openai.organization = "org-7IOSzoKvbgeBrwuhdlXR7JSB"
openai.api_key = "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"

from fastapi import FastAPI  

app = FastAPI()
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/emails/")
async def create_email(email_prompt: dict):
    req = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": email_prompt["email_prompt"]}])
    if req:
        email_output = req.choices[0].message.content
        # email_split = email_output.split("\n")
        # for i in range(len(email_split)):
        #     email_split[i] = "<p>" + email_split[i] + "</p>"
        # email_output = "".join(email_split)
        return email_output
    else:
        raise HTTPException(404, f"Invalid Request")