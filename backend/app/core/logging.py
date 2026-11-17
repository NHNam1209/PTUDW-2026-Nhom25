import contextvars
import logging
import logging.handlers
import os
import sys
from typing import Optional

# Context variable to hold correlation_id per async task/request
correlation_id_ctx: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar(
    "correlation_id", default="-"
)


class CorrelationIdFilter(logging.Filter):
    """Logging filter that injects the current request correlation_id into log records."""

    def filter(self, record: logging.LogRecord) -> bool:
        record.correlation_id = correlation_id_ctx.get() or "-"
        return True


def setup_logging(logs_dir: str = "logs") -> logging.Logger:
    """Configures structured system logging with console and rotating file handlers."""
    os.makedirs(logs_dir, exist_ok=True)

    log_format = (
        "[%(asctime)s] [%(levelname)-8s] [CorrID: %(correlation_id)s] "
        "[%(name)s] %(message)s"
    )
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

    corr_filter = CorrelationIdFilter()

    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if setup_logging is called multiple times
    if not root_logger.handlers:
        # 1. Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        console_handler.addFilter(corr_filter)
        root_logger.addHandler(console_handler)

        # 2. General App Log File (Rotating at 10MB, keep 5 backups)
        app_file_handler = logging.handlers.RotatingFileHandler(
            filename=os.path.join(logs_dir, "app.log"),
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8",
        )
        app_file_handler.setLevel(logging.INFO)
        app_file_handler.setFormatter(formatter)
        app_file_handler.addFilter(corr_filter)
        root_logger.addHandler(app_file_handler)

        # 3. Error Log File (Rotating at 10MB, keep 5 backups)
        error_file_handler = logging.handlers.RotatingFileHandler(
            filename=os.path.join(logs_dir, "error.log"),
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8",
        )
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(formatter)
        error_file_handler.addFilter(corr_filter)
        root_logger.addHandler(error_file_handler)

    # 4. Dedicated Audit Trail Logger
    audit_logger = logging.getLogger("culinary_blog.audit")
    audit_logger.setLevel(logging.INFO)
    audit_logger.propagate = True  # also goes to app.log and console

    audit_file_path = os.path.join(logs_dir, "audit.log")
    # Check if audit handler already attached
    if not any(
        isinstance(h, logging.handlers.RotatingFileHandler) and h.baseFilename == os.path.abspath(audit_file_path)
        for h in audit_logger.handlers
    ):
        audit_file_handler = logging.handlers.RotatingFileHandler(
            filename=audit_file_path,
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8",
        )
        audit_file_handler.setLevel(logging.INFO)
        audit_file_handler.setFormatter(formatter)
        audit_file_handler.addFilter(corr_filter)
        audit_logger.addHandler(audit_file_handler)

    logger = logging.getLogger("culinary_blog")
    logger.info("Structured logging initialized successfully with file rotation.")
    return logger

