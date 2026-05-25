from pydantic import BaseModel
from typing import Optional, Dict, Any


class InvoiceResponse(BaseModel):
  invoice_valid: bool
  data: Optional[Dict[str, Any]] = None


class InvoiceDB(BaseModel):
  url: str
  user_id: int
  content: str
