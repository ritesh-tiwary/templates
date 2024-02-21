# docker ps
# docker stop CONTAINER_ID
# docker rm CONTAINER_ID

# docker build -t fastapi.app .
# docker run -d -p 8000:8000 fastapi.app:latest
# docker-compose up -d --build --scale fastapi.app=3
# docker compose -p fastapi_app logs

# docker compose -p fastapi_app -f docker-compose.yml up -d --build --scale fastapi.app=4

uvicorn app:app --proxy-headers --host 0.0.0.0 --port 8000 --reload
