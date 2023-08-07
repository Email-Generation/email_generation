from app.config.settings import settings
from app.routes.email_routes import router as email_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from mangum import Mangum

app = FastAPI(title=settings.title, description=settings.description)
handler = Mangum(app)


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
