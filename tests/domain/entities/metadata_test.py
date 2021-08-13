import freezegun
from datetime import datetime, timedelta, timezone

from autifycli.domain.entities.metadata import Metadata


JST = timezone(timedelta(hours=+9), "JST")


@freezegun.freeze_time('2021-08-12')
def test_metadata():
    site = "https://example.com"
    num_links = 0
    num_images = 0
    last_fetch = datetime.now(JST)

    meta = Metadata(site=site, last_fetch=last_fetch)
    assert site == meta.site
    assert num_links == meta.num_links
    assert num_images == meta.num_images
    assert str(last_fetch) == str(meta.last_fetch)
    assert site in str(meta)
