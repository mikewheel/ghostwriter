"""
Module for project-level configuration.
"""
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
S3_BUCKET = "cs4120-final-project-data"

WRITE_TEMP_PROGRESS = True
