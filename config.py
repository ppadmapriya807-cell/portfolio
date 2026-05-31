"""
==============================================
  Configuration Settings for Portfolio App
==============================================
  Reads from environment variables for
  security. Falls back to defaults for local
  development only.
==============================================
"""

import os
from dotenv import load_dotenv

# Load .env file if it exists (for local development)
load_dotenv()


class Config:
    """Base configuration class."""

    # ── Flask ──────────────────────────────────────────────────────────────
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.environ.get('FLASK_DEBUG', 'True') == 'True'

    # ── MySQL ──────────────────────────────────────────────────────────────
    MYSQL_HOST     = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER     = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'your_password_here')
    MYSQL_DB       = os.environ.get('MYSQL_DB', 'portfolio_db')
    MYSQL_PORT     = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_CURSORCLASS = 'DictCursor'

    # ── Upload Settings ────────────────────────────────────────────────────
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload


class ProductionConfig(Config):
    """Production configuration — debug OFF."""
    DEBUG = False


class DevelopmentConfig(Config):
    """Development configuration — debug ON."""
    DEBUG = True
