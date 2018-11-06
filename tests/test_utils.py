"""Test utils."""
import pytest
import requests

from vectra_api_client import utils


@pytest.mark.parametrize('prefix_url', [
    'http://localhost',
    'http://localhost/',
    'http://localhost//',
])
def test_prefix_url_session(mocker, prefix_url):
    mocker.patch('requests.Session.request')

    s = utils.PrefixUrlSession(prefix_url)
    s.request('GET', 'endpoint')
    requests.Session.request.assert_called_with(
        'GET', '{}/endpoint'.format(prefix_url.rstrip('/'))
    )
