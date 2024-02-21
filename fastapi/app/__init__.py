import time
from app.logger import Logger
from app.routers import users, processes
from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError


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
    request_id = request.headers.get("X-Request-Id")
    logger.info(f"Request Id: {request_id}")
    logger.info(f"Request Path: {request.url.path}")
    try:
        start_time = time.time()
        response = await call_next(request)
        response_time = time.time() - start_time
        response.headers["X-Response-Time"] = str(response_time)
        logger.info(f"Response Time(ms): {response_time}")
        logger.info(f"Response Status Code: {response.status_code}")
        return response
    except Exception as exc:
        logger.error(f"Error: {exc}")
        raise

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {}
    error = exc.errors()
    errors["type"] = error[0]["type"]
    errors["msg"] = error[0]["msg"]
    errors["loc"] = error[0]["loc"]
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": errors})
