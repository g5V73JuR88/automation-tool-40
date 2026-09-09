import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FILE = Path("automation-tool-40.log")

def setup_logger(name: str = "automation-tool") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=5_000_000, 
            backupCount=3
        )
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger