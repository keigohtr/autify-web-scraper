import pytest

from autifycli.domain.utils import url2filepath
from autifycli.exceptions import UnsupportedUrlTypeException


def test_url2filepath_happycase():
    url = "https://example.com"
    r = url2filepath(url)
    assert "example.com.html" == str(r)


def test_url2filepath_invalid_url():
    url = "example.com"
    with pytest.raises(UnsupportedUrlTypeException) as e:
        url2filepath(url)
        assert "Invalid URL." == str(e)


def test_url2filepath_slash_included():
    url = "https://example.com/hoge"
    with pytest.raises(UnsupportedUrlTypeException) as e:
        url2filepath(url)
        assert 'We don\'t support "/" containing URL yet.' == str(e)

    url = "https://example.com/"
    with pytest.raises(UnsupportedUrlTypeException) as e:
        url2filepath(url)
        assert 'We don\'t support "/" containing URL yet.' == str(e)


def test_url2filepath_query_included():
    url = "https://example.com/hoge?a=b&b=c"
    with pytest.raises(UnsupportedUrlTypeException) as e:
        url2filepath(url)
        assert "We don't support query parameter containing URL yet." == str(e)
