import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from app.config.settings import settings
from app.routes.email_routes import router as email_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from mangum import Mangum

app = FastAPI(
    title=settings.title,
    description=settings.description,
    version="1.0.0",
    # terms_of_service="URL to terms of service",
    contact=[{"name": "Kayvan Shah",# "url": "Contact URL 1",
            "email": "kayvan.shah@usc.edu", },
        {
            "name": "Bhumi Godiwala",
            # "url": "Contact URL 2",
            "email": "bhumi.godiwala@usc.edu",
        },
    ],
    # license_info={"name": "BSD 3-Clause License", "url": "License URL"},
    lifespan=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/docs")


# Add all of the routes to the application
app.include_router(email_router, tags=["Emails"])

handler = Mangum(app)
