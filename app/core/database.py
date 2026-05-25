from postgrest import SyncPostgrestClient

from app.core.config import settings
from typing import Generator

class DatabaseService:
  """Handles database operations."""
  def __init__(self):
    
    if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
      raise ValueError("Missing Supabase credentials")

    self.rest_url = settings.SUPABASE_URL
    self.service_key = settings.SUPABASE_KEY 
    
    self.client = SyncPostgrestClient

  def connect(self) -> SyncPostgrestClient:
    self.client = SyncPostgrestClient(
      self.rest_url,
      headers = {
        'apiKey': self.service_key,
        'Authorization': f"Bearer {self.service_key}",
        'schema': 'public'
      }
    )

  def disconnect (self):
    if (self.client):
      self.client.close()

db_manager = DatabaseService()

def get_db() -> Generator[SyncPostgrestClient, None, None]:
  client = db_manager.connect()
  
  try:
    yield client
  finally:
    db_manager.disconnect()