```
sudo apt-get update && sudo apt-get install -y tmux
```

```
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4 --loop uvloop --http httptools --interface asgi3 --proxy-headers --no-date-header --no-server-header --no-access-log
```

```
gunicorn app:app --bind 0.0.0.0:8000 --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

```
docker build --tag --file Dockerfile grpc-async-server .
```

```
docker run --publish 50051:50051 --detach grpc-async-server
```
