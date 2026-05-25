import cloudinary
import cloudinary.uploader

from app.core.config import settings
from fastapi import UploadFile


# Configure Cloudinary
cloudinary.config(
  cloud_name=settings.CLOUDINARY_CLOUD_NAME,
  api_key=settings.CLOUDINARY_API_KEY,
  api_secret=settings.CLOUDINARY_API_SECRET,
  secure=True
)


class CloudinaryService:
  """Handles file uploads to Cloudinary."""

  @staticmethod
  def upload_file(file_path: str, original_filename: str) -> str:
    """
    Upload a local file to Cloudinary and return its public URL.

    Args:
      file_path: Path to the local file to upload.
      original_filename: Original name of the uploaded file.

    Returns:
      The secure URL of the uploaded file.
    """
    result = cloudinary.uploader.upload(
      file_path,
      folder="digi-docs",
      resource_type="auto",
    )

    return result["secure_url"]
