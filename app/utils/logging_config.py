import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.config import settings


def setup_logging() -> logging.Logger:
    """Configure application logging."""
    log_path = Path(settings.log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # TODO: implement.
    # Note: The log directory creation logic is already
    # implemented above, you don't have to care about it.
    # Just implement the logging configuration directly below.

    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler(
                log_path,
                maxBytes=settings.log_max_bytes,
                backupCount= settings.log_backup_count
            ),
            logging.StreamHandler(),
        ],
    )

    return logging.getLogger(settings.app_name)