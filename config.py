import os

# API Configurations for Local Testing
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_MODEL = "llama3-8b-instruct"

# Directory paths for sandbox data
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
