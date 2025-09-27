import logging
import logging.config
from pathlib import Path

config_path = Path(__file__).parent.parent / 'logging_config.ini'
logging.config.fileConfig(config_path)

# Використання логера
logger = logging.getLogger('sampleLogger')
