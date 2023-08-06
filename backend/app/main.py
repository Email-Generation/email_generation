from app.config.settings import Settings
from app.routes.email_routes import router as email_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

# Load settings from the .env file
settings = Settings()

app = FastAPI(title=settings.title, description=settings.description)
handler = Mangum(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add all of the routes to the application
app.include_router(email_router, tags=["Emails"])
