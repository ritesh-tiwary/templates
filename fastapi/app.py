import os
import uvicorn
from typing import List
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()
ALLOWED_EXTENSIONS = {"txt", "csv", "xlsx", "zip"}
valid_file = lambda filename: "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.get("/", response_class=HTMLResponse)
async def get_upload_form():
    """
    Serve the HTML upload form.
    """
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>File Upload</title>
    </head>
    <body>
        <h1>File Upload</h1>
        <form action="/uploads/" method="post" enctype="multipart/form-data">
            <label for="file">Select file(s) to upload:</label><br>
            <input type="file" id="file" name="files" multiple accept=".txt, .csv, .xlsx, .zip"><br><br>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    """

@app.post("/uploads/")
async def upload_files(files: List[UploadFile] = File(...)):
    """
    Endpoint to upload a file.
    http://127.0.0.1:5000

    - Dependencies
        pip install --upgrade fastapi
        pip install --upgrade uvicorn
        pip install --upgrade python-multipart
    """
    uploaded_filenames = []
    for file in files:
        if valid_file(file.filename):
            # Ensure file is being processed in chunks to handle large files
            with open(os.path.join("data", file.filename), "wb") as buffer:
                while True:
                    chunk = await file.read(65536)      # 64 KB chunks
                    if not chunk: break
                    buffer.write(chunk)
            uploaded_filenames.append(file.filename)
        else:
            raise HTTPException(status_code=400, detail=f"{file.filename.rsplit('.', 1)[1].capitalize()} files are not allowed.")

    return {"Uploaded Files": uploaded_filenames}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
