"""
Autify Web Scraper
Keigo Hattori
"""
from typing import List

import click

import autifycli.version
from autifycli.domain.services.fetch_service import fetch_pages

__version__ = autifycli.version.VERSION


@click.group(help="Autify command line interface")
@click.version_option(version=__version__, message="v%(version)s")
@click.pass_context
def main(ctx: click.Context) -> None:
    pass


@main.command(name="fetch", short_help="fetch web pages")
@click.option("--metadata", "metadata", help="Display metadata of url", is_flag=True)
@click.option("-p", "--numof-process", "numof_process", help="Number of processes.", type=int, default=1)
@click.argument("urls", nargs=-1, required=True)
def fetch(metadata: bool, numof_process: int, urls: List[str]) -> None:
    """Fetch web pages"""
    fetch_pages(metadata, numof_process, set(urls))


if __name__ == "__main__":
    main()
