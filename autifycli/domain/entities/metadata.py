"""
Autify Web Scraper
Keigo Hattori
"""
import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), "JST")


@dataclass
class Metadata:
    """Metadata"""

    site: str
    num_links: int = 0
    num_images: int = 0
    last_fetch: datetime = datetime.now(JST)

    def __str__(self) -> str:
        rtn = {
            "site": self.site,
            "last_fetch": str(self.last_fetch),
            "num_links": self.num_links,
            "num_images": self.num_images,
        }
        return json.dumps(rtn, indent=2)
