from app.logger import Logger
from app.routers import users, processes
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


logger = Logger()
app = FastAPI()
app.include_router(users.router)
app.include_router(processes.router)

# Mount the 'static' directory as a static directory to use on UX
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=open("app/templates/index.html", "r").read())

@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    request_id = request.headers.get("X-Request-Id", "")
    logger.info(f"Request to {request.url.path}")
    try:
        response = await call_next(request)
        logger.info(f"Response with status code {response.status_code}")
        return response
    except Exception as exc:
        logger.error(f"Error: {exc}")
        raise
