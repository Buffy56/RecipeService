from fastapi import FastAPI
from app.api import example
from app.config import settings

app = FastAPI()
app.include_router(example.router)

print(f"Starting RecipeService in {settings.APP_ENV} mode...")

@app.get("/")
def read_root():
    return {"env": settings.APP_ENV}
