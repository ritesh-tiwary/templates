import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("grpc_server.log"),  # ✅ Save to a file
        logging.StreamHandler()  # ✅ Also print to console
    ]
)
