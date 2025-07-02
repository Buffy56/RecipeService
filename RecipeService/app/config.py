from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_ENV = os.getenv("APP_ENV", "development")
    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()
