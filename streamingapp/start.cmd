:: !/bin/command
:: Usage: start.cmd

py -m venv streamingapp-venv

.\streamingapp-venv\Scripts\activate && py -m pip install --upgrade pip && py -m pip install --use-pep517 -qr requirements.txt && uvicorn app:app --host localhost --port 8000
