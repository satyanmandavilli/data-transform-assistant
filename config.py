# src/app/config.py
from dotenv import load_dotenv
import os

load_dotenv()

# File and Size settings
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
SUPPORTED_FORMATS = ['csv', 'xlsx']

# Processing settings
BATCH_SIZE = 50

# Databricks Configuration
DATABRICKS_CONFIG = {
    'DATABRICKS_SERVER_HOSTNAME': os.getenv('DATABRICKS_SERVER_HOSTNAME'),
    'DATABRICKS_HTTP_PATH': os.getenv('DATABRICKS_HTTP_PATH'),
    'DATABRICKS_ACCESS_TOKEN': os.getenv('DATABRICKS_ACCESS_TOKEN'),
    'DATABRICKS_LLM_MODEL': os.getenv('DATABRICKS_LLM_MODEL')
}