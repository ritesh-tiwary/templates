# docker build -t fastapi.app .
# docker run -d -p 8000:8000 fastapi.app:latest

# docker-compose up -d --build --scale fastapi.app=3
# docker compose -p fastapi_app logs
# docker compose -p fastapi_app -f docker-compose.yml up -d --build --scale fastapi.app=3
uvicorn app:app --host localhost --port 8000 --reload
