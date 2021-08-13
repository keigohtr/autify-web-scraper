import tempfile

from unittest.mock import patch
import pytest
import requests_mock

from autifycli.domain.services.fetch_service import _fetch_page_process, FETCH_RETRY_ATTEMPT_NUMBER
from autifycli.exceptions import InternalServerErrorException
from requests.exceptions import ConnectionError, MissingSchema
from autifycli.exceptions import ClientErrorException, InternalServerErrorException, UnsupportedUrlTypeException


@pytest.fixture
def req_mock(request):
    m = requests_mock.Mocker()
    m.start()
    request.addfinalizer(m.stop)
    return m


def test_fetch_page_process_happycase(req_mock):
    url = "https://example.com"
    metadata = True
    expected_content= "<html><head></head><body></body></html>"

    req_mock.register_uri('GET', url, text=expected_content)
    with tempfile.NamedTemporaryFile('w') as wf:
        with patch('autifycli.domain.services.fetch_service.url2filepath') as mock_url2filepath:
            mock_url2filepath.return_value = wf.name
            _fetch_page_process(url, metadata)

    assert req_mock.called


def test_fetch_page_process_500(req_mock):
    url = "https://example.com"
    metadata = True

    req_mock.register_uri('GET', url, status_code=500)
    with pytest.raises(InternalServerErrorException):
        _fetch_page_process(url, metadata)

    assert req_mock.call_count == FETCH_RETRY_ATTEMPT_NUMBER


def test_fetch_page_process_404(req_mock):
    url = "https://example.com"
    metadata = True

    # ClientErrorException
    req_mock.register_uri('GET', url, status_code=404)
    _fetch_page_process(url, metadata)


def test_fetch_page_process_invalid_url(req_mock):
    # ConnectionError
    url = "https://dummmmmmmmy.coooooom"
    metadata = True
    _fetch_page_process(url, metadata)

    # MissingSchema
    url = "hoge"
    _fetch_page_process(url, metadata)

    # UnsupportedUrlTypeException
    url = "https://example.com/invalid"
    expected_content= "<html><head></head><body></body></html>"
    req_mock.register_uri('GET', url, text=expected_content)
    _fetch_page_process(url, metadata)

    # Exception
    with patch('autifycli.domain.services.fetch_service.url2filepath') as mock_url2filepath:
        mock_url2filepath.side_effect = Exception()
        _fetch_page_process(url, metadata)
