"""
Autify Web Scraper
Keigo Hattori
"""
import click
from typing import List

import autifycli.version
from autifycli.logger import get_logger


__version__ = autifycli.version.VERSION
logger = get_logger()


@click.group(help='Autify command line interface')
@click.version_option(version=__version__, message='v%(version)s')
@click.pass_context
def main(ctx):
    pass


@main.command(name='fetch', short_help='fetch web pages')
@click.option('--metadata', 'metadata', help="Display metadata of url", is_flag=True)
@click.argument('urls', nargs=-1, required=True)
def fetch(metadata: bool, urls: List[str]):
    """Fetch web pages

    Args:
        metadata (bool): flag for whether to display metadata; site, num_links, num_images, last_fetch.
        urls (List[str]): URLs to fetch.
    """
    click.echo (metadata)
    for url in urls:
        click.echo (url)

    click.echo("Done")


if __name__ == '__main__':
    main()
