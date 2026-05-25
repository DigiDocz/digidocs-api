from pathlib import Path
from google import genai
from google.genai import types
from typing import Optional

from app.core.config import settings
from app.features.extractor.schema import InvoiceResponse


class Extractor:
  def __init__(self, file_path: str):
    self.file_path = file_path
    self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

  def extract_invoice(self) -> Optional[InvoiceResponse]:
    print(f"Extracting invoice from {self.file_path}")

    try:
      upload_file = self.client.files.upload(file=Path(self.file_path))

      response = self.client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=[
          "Determine if this document is a valid invoice. Return a JSON object with 'invoice_valid' (boolean). If it is a valid invoice, extract all fields, tables, and text into a 'data' key. If it is NOT an invoice, set 'invoice_valid' to false and 'data' to null.",
          upload_file
        ],
        config=types.GenerateContentConfig(
          response_mime_type="application/json"
        )
      )

      return InvoiceResponse.model_validate_json(response.text)
    except Exception as e:
      print(f"Error: {str(e)}")
      return None
