import os
import uvicorn
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, status, File, UploadFile, HTTPException
from app.logger import AppLogger
from aiologger.utils import CallableWrapper


app = FastAPI()
logger = AppLogger()
# Mount the 'static' directory as a static directory to use on UX
app.mount("/static", StaticFiles(directory="app/static"), name="static")

ALLOWED_EXTENSIONS = {"txt", "csv", "xlsx", "zip"}
valid_file = lambda filename: "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


async def set_context(request_id):
    context = {"request_id": request_id}
    return context

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=open("app/templates/index.html", "r").read())

@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", "")
    # logger.info(CallableWrapper(set_context))
    logger.info(f"Request to {request.url.path}")
    try:
        response = await call_next(request)
        print(response)
        logger.info(f"Response with status code {response.status_code}")
        return response
    except Exception as exc:
        logger.error(f"Error: {exc}")
        raise

@app.post("/uploads/")
async def upload_files(files: List[UploadFile] = File(...)):
    """
    Endpoint to upload a file.
    http://127.0.0.1:5000
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
                raise HTTPException(status_code=400, detail=f"{file.filename.rsplit('.', 1)[1].capitalize()} files are not allowed.")

        logger.info(f"Total files uploaded: {len(uploaded_filenames)}")
        return {"File Count": len(uploaded_filenames), "Files": uploaded_filenames}
    except Exception as exc:
        logger.error(f"Error uploading files: {exc}")
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail="Failed to upload files")
