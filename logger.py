import logging
import os
from datetime import datetime

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
log_filename = f"logs/log_{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(event: str):
    logging.info(event)