"""
Autify Web Scraper
Keigo Hattori
"""
import time
from multiprocessing import Pool
from typing import Set

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError, MissingSchema
from retrying import retry

from autifycli.domain.entities.metadata import Metadata
from autifycli.domain.utils import url2filepath
from autifycli.exceptions import ClientErrorException, InternalServerErrorException, UnsupportedUrlTypeException
from autifycli.logger import logger

FETCH_RETRY_ATTEMPT_NUMBER = 3


@retry(stop_max_attempt_number=FETCH_RETRY_ATTEMPT_NUMBER)
def _fetch_page_process(url: str, metadata: bool) -> None:
    try:
        meta = Metadata(site=url)
        html = requests.get(url)
        if html.status_code >= 400 and html.status_code < 500:
            raise ClientErrorException()
        if html.status_code >= 500:
            raise InternalServerErrorException()

        soup = BeautifulSoup(html.text, "html.parser")

        filepath = url2filepath(url)
        with open(filepath, "w") as wf:
            wf.write(str(soup))

        if metadata:
            meta.num_links = len(soup.find_all("a", href=True))
            meta.num_images = len(soup.find_all("img"))
            print(meta)
    except InternalServerErrorException as e:
        # Retry
        logger.error(f'Internal Server Error. Retry up to {FETCH_RETRY_ATTEMPT_NUMBER} times. "{url}"')
        time.sleep(1)
        raise e
    except (MissingSchema, ConnectionError):
        logger.error(f'Invalid URL. "{url}"')
    except ClientErrorException:
        logger.error(f'4xx Client Error. "{url}"')
    except UnsupportedUrlTypeException as e:
        logger.error(e)
    except Exception:
        logger.error(f'Unexpected Error. "{url}"')


def fetch_pages(metadata: bool, numof_process: int, urls: Set[str]) -> None:
    p = Pool(numof_process)
    for url in urls:
        p.apply_async(_fetch_page_process, args=(url, metadata))
    # Runnining process asynchronously
    p.close()
    p.join()
    # All processes have finished.
