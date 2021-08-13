"""
Autify Web Scraper
Keigo Hattori
"""
import logging


def get_logger():
    """
    Return a logger to output to stderr and logging file

    :return: (Logger) Logger.
    """
    # Initialize if this function is called at first.
    if not get_logger.initialized:
        logger = logging.getLogger("autifycli")
        logger.setLevel(logging.DEBUG)

        # stderr
        echo = logging.StreamHandler()
        echo.setLevel(logging.ERROR)
        echo.setFormatter(logging.Formatter(
            "%(asctime)s %(levelname)8s %(message)s"))

        logger.addHandler(echo)

        # Finish initialize.
        get_logger.initialized = True

    # Return existent logger if it has been already created.
    return logging.getLogger("autifycli")


get_logger.initialized = False
