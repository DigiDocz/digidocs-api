import os
import tempfile
import shutil

from fastapi import APIRouter, UploadFile, HTTPException

from app.features.extractor.service import Extractor
from app.core.cloudinary import CloudinaryService

router = APIRouter(prefix='/docs', tags=['Docs'])

@router.post('/extract')
async def extract(file: UploadFile):
  # Save uploaded file to a temp location
  suffix = os.path.splitext(file.filename or "")[1]
  with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
    shutil.copyfileobj(file.file, tmp)
    tmp_path = tmp.name

  try:
    # Upload to Cloudinary
    file_url = CloudinaryService.upload_file(tmp_path, file.filename or "document")

    # Extract invoice data using the local temp file
    extractor = Extractor(file_path=tmp_path)
    result = extractor.extract_invoice()

    if result is None:
      raise HTTPException(status_code=422, detail="Failed to extract invoice data")

    return {
      "file_url": file_url,
      "extraction": result
    }
  finally:
    os.unlink(tmp_path)
