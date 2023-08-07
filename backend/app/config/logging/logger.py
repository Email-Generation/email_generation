import json
import logging
import logging.config
import os

import yaml

from app.config.settings import settings

# Creating constant paths for logging
DEFAULT_LOGGING_CONFIG_PATH = os.path.join(
    settings.DEFAULT_LOGGING_CONFIG_DIR, "logging.yaml"
)


def read_config(metadata_path: str) -> dict:
    """This function reads the metadata from a JSON or YAML file

    Args:
        metadata_path (str): Path to metadata JSON or YAML file

    Returns:
        dict: The JSON configuration file
    """
    with open(metadata_path, "r") as f:
        if metadata_path.split(".") == "json":
            return json.load(f)
        return yaml.load(f, Loader=yaml.SafeLoader)


def setup_logging():
    """Setup Logging via Logging YAML file"""
    logging_config = read_config(DEFAULT_LOGGING_CONFIG_PATH)
    logging.config.dictConfig(logging_config)


setup_logging()


def get_simple_logger(name: str) -> logging.Logger:
    """Get the default logger

    Args:
        name (str): Name of logger

    Returns:
        logging.Logger
    """
    logger = logging.getLogger(name)
    return logger


def get_logger(name: str = None) -> logging.Logger:
    """
    Get a `email_generation` logger. For use within Weather Combiner.

    Args:
        name (str): Name of logger

    Returns:
        logging.Logger: Logger with the defined name
    """

    parent_logger = logging.getLogger("email_generation")

    if name:
        if not name.startswith(parent_logger.name + "."):
            logger = parent_logger.getChild(name)
        else:
            logger = logging.getLogger(name)
    else:
        logger = parent_logger

    return logger
