# docker build -t flask.app .
# docker run -d -p 5000:5000 flask.app:latest

# docker-compose up -d --build --scale flask.app=3
# docker compose -p flask_app logs
# docker compose -p flask_app -f docker-compose.yml up -d --build --scale flask.app=3
uvicorn app:app --host localhost --port 5000
