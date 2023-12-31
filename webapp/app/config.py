import os
import secrets


# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the download directory
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR")

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = secrets.token_hex()
