import os
from app.logger import Logger
from typing import List, Annotated
from app.dependencies import get_request_id_header, get_checksum_header
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile, Response


router = APIRouter(
    prefix="/processes",
    tags=["processes"],
    dependencies=[Depends(get_request_id_header), Depends(get_checksum_header)],
    responses={404: {"Description": "Not found"}}
    )

logger = Logger()
ALLOWED_EXTENSIONS = {"txt", "csv", "xlsx", "zip"}
valid_file = lambda filename: "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@router.post("/uploads/", status_code=status.HTTP_201_CREATED)
async def upload_files(response: Response, files: Annotated[List[UploadFile], File(description="Choose a valid file to upload")]):
    """
    Endpoint to upload a file.

    - **X-Request-Id**: A 36-character UUID (Universal Unique Identifier) is hexadecimal number that is generated for each request.

            7cd35adb-1484-2348-df3e-f077cd6ff34d

    - **X-Checksum**: A 32-character MD5 checksum is hexadecimal number that is computed on a file.

            52b7d61828e5cc56726f25f49ea5d6d3
    \f
    :files: User input.
    """
    try:
        uploaded_filenames = []
        for file in files:
            if valid_file(file.filename):
                # Ensure file is being processed in chunks to handle large files
                with open(os.path.join("app/data", file.filename), "wb") as buffer:
                    while True:
                        chunk = await file.read(65536)      # 64 KB chunks
                        if not chunk: break
                        buffer.write(chunk)
                uploaded_filenames.append(file.filename)
            else:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"detail": f"{file.filename.rsplit('.', 1)[1].capitalize()} files are not allowed."}

        logger.info(f"Total files uploaded: {len(uploaded_filenames)}")
        return {"File Count": len(uploaded_filenames), "Files": uploaded_filenames}
    except Exception as exc:
        logger.error(f"Failed to upload files: {exc}")
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to upload files")
