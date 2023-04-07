from fastapi import HTTPException, status


crop_not_found_exc = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Crop not found"
)
