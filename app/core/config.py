import logging
import sys
from typing import List
import os

from databases import DatabaseURL
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from app.core.logging import InterceptHandler

API_PREFIX = '/api'

JWT_TOKEN_PREFIX = 'Token'
VERSION = '0.0.0'

config = Config('.env')

DEBUG: bool = config('DEBUG', cast=bool, default=False)

DATABASE_URL: DatabaseURL = config('DB_CONNECTION', cast=DatabaseURL, default=os.environ.get('DB_CONNECTION'))
MAX_CONNECTIONS_COUNT: int = config('MAX_CONNECTIONS_COUNT', cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config('MIN_CONNECTIONS_COUNT', cast=int, default=10)

SECRET_KEY: Secret = config('SECRET_KEY', cast=Secret, default=os.environ.get('SECRET_KEY'))

PROJECT_NAME: str = config('PROJECT_NAME', cast=str, default='FastAPI example')
ALLOWED_HOSTS: List[str] = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings, default='')

# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL)
logger.configure(handlers=[{'sink': sys.stderr, 'level': LOGGING_LEVEL}])






















