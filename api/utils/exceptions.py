from fastapi import HTTPException, status


crop_not_found_exc = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Crop not found"
)
land_not_found_exc = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Land not found"
)

land_missing_details_exc = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Land has missing details. Can't do prediction.",
)
