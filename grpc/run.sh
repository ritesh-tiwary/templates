#!/bin/bash

tmux new-session -d -s mysession
tmux send-keys -t mysession "python server.py" C-m
tmux split-window -h -t mysession
tmux send-keys -t mysession "uvicorn app:app --host 0.0.0.0 --port 8000 --workers 1 --loop uvloop --http httptools --interface asgi3 --proxy-headers --no-date-header --no-server-header --no-access-log" C-m
tmux attach -t mysession