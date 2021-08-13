from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner

from autifycli.cmd import fetch


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.parametrize(
    "cmd",
    [
        (["--metadata", "-p", "2", "https://example.com"]),
        (["-p", "2", "https://example.com"]),
        (["--metadata", "https://example.com"]),
        (["https://example.com", "https://dummy.com"]),
    ],
)
@patch("autifycli.cmd.fetch_pages", MagicMock(return_value=None))
def test_fetch_happycase(runner, cmd):
    r = runner.invoke(fetch, cmd)
    assert r.exit_code == 0


@pytest.mark.parametrize(
    "cmd",
    [
        (["-p", "hoge", "https://example.com"]),
        ([]),
    ],
)
def test_fetch_invalid(runner, cmd):
    r = runner.invoke(fetch, cmd)
    assert r.exit_code == 2
