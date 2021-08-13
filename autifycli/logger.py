"""
Autify Web Scraper
Keigo Hattori
"""
import logging


def get_logger() -> logging.Logger:
    """
    Return a logger to output to stderr and logging file

    :return: (Logger) Logger.
    """
    logger = logging.getLogger("autifycli")
    logger.setLevel(logging.DEBUG)

    # stderr
    echo = logging.StreamHandler()
    echo.setLevel(logging.ERROR)
    echo.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

    logger.addHandler(echo)

    # Return existent logger if it has been already created.
    return logging.getLogger("autifycli")


logger = get_logger()
