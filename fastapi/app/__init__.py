import time
from app.logger import Logger
from app.routers import users, processes, tasks
from fastapi import FastAPI, Request, Response, status, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError, ResponseValidationError


logger = Logger()

description = """
ComplianceApp API helps you do awesome stuff. 🚀

## Users
You will be able to:
* **Create users**.
* **Read users** (_not implemented_).

## Processes
You will be able to:
* **Upload files**.
* **Download files** (_not implemented_).

## Tasks
You will be able to:
* **Generate Token**.
* **Validate Token** (_not implemented_).
"""

app = FastAPI(
    title="ComplianceApp",
    description=description,
    docs_url="/documentation",
    summary="Compliance Applications help users to get clear visibility into the information and documents required.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Ritesh Tiwary",
        "url": "http://example.com/contact/",
        "email": "ritesh.tiwary@rediffmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
    )

app.include_router(users.router)
app.include_router(processes.router)
app.include_router(tasks.router)

# Mount the 'static' directory as a static directory to use on UX
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Redirect to Swagger UI
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/documentation")

@app.get("/home", include_in_schema=False, response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=open("app/templates/index.html", "r").read())

@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    received_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    request_id = request.headers.get("X-Request-Id")
    user_agent = request.headers.get("user-agent")
    # request_body = await request.body()
    # logger.info(f"Body: {request_body.decode()}")
    
    try:
        start_time = time.time()
        response = await call_next(request)
        response_time = time.time() - start_time
        response.headers["X-Response-Time"] = str(response_time)

        log = {
            "RequestId": request_id,
            "Received": received_at,
            "Severity": "Informational",
            "From": request.client.host,
            "User-Agent": user_agent,
            "Method": request.method,
            "Base-Url": str(request.base_url),
            "Path": request.url.path,
            "Response-Time": response_time,
            "Status-Code": response.status_code
        }
        logger.info(log)
        return response
    except Exception as exc:
        log = {
            "RequestId": request_id,
            "Received": received_at,
            "Severity": "Error",
            "From": request.client.host,
            "User-Agent": user_agent,
            "Method": request.method,
            "Base-Url": str(request.base_url),
            "Path": request.url.path,
            "Response": str(exc),
            "Status-Code": 500
        }
        logger.error(log)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to process the request") 
    
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {}
    error = exc.errors()
    errors["type"] = error[0]["type"]
    errors["loc"] = error[0]["loc"]
    errors["msg"] = error[0]["msg"]
    errors["input"] = error[0]["input"]
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": errors})

@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(response: Response, exc: ResponseValidationError):
    errors = {}
    error = exc.errors()
    errors["type"] = error[0]["type"]
    errors["loc"] = error[0]["loc"]
    errors["msg"] = error[0]["msg"]
    errors["input"] = error[0]["input"]
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": errors})
