"""
Autify Web Scraper
Keigo Hattori
"""
from pathlib import Path
from urllib.parse import urlparse

from autifycli.exceptions import UnsupportedUrlTypeException


def url2filepath(url: str) -> Path:
    """URL to Filepath

    Args:
        url (str): URL

    Returns:
        Path: File to save
    """
    parsed_url = urlparse(url)

    if not parsed_url.netloc:
        raise UnsupportedUrlTypeException('Invalid URL.')
    # TODO: Support both following cases.
    if "/" in parsed_url.path:
        raise UnsupportedUrlTypeException('We don\'t support "/" containing URL yet.')
    if parsed_url.query:
        raise UnsupportedUrlTypeException('We don\'t support query parameter containing URL yet.')

    return Path(f'{parsed_url.netloc}.html')
