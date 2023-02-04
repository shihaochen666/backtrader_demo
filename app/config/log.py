import logging
import os
import sys

from loguru import logger

from hans import InterceptHandler

LOGGING_LEVEL = logging.DEBUG if logging.DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")
curPath = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = curPath[:curPath.find('app') + len('app')]
logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

log_file_path = os.path.join(BASE_DIR, 'logs/wise.log')
err_log_file_path = os.path.join(BASE_DIR, 'logs/wise.err.log')

loguru_config = {
    "handlers": [
        {"sink": sys.stderr, "level": "INFO",
         "format": "<green>{time:YYYY-mm-dd HH:mm:ss.SSS}</green> | {thread.name} | <level>{level}</level> | "
                   "<cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"},
        {"sink": log_file_path, "rotation": "500 MB", "encoding": 'utf-8'},
        {"sink": err_log_file_path, "serialize": True, "level": 'ERROR', "rotation": "500 MB",
         "encoding": 'utf-8'},
    ],
}
logger.configure(**loguru_config)
