from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  GEMINI_API_KEY: str
  CLOUDINARY_CLOUD_NAME: Optional[str] = None
  CLOUDINARY_API_KEY: Optional[str] = None
  CLOUDINARY_API_SECRET: Optional[str] = None
  SUPABASE_URL: Optional[str] = None
  SUPABASE_KEY: Optional[str] = None


  class Config:
    env_file = ".env"
    extra = "ignore"

settings = Settings()
