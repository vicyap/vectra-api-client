#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `vectra_api_client` package."""

import pytest
import requests

from vectra_api_client import clients


def get_client(version):
    if version == 1:
        return clients.DetectClient(url='', username='', password='')
    elif version == 2:
        return clients.DetectClient(url='', token='')


@pytest.mark.parametrize('attrs,methods,version', [
    (['settings'], ['get'], 1),
    (['rules'], ['get'], 1),
    (['rules'], ['get', 'post', 'put', 'delete', 'options'], 2),
    (['detections'], ['get'], 1),
    (['detections'], ['get', 'patch'], 2),
    (['hosts'], ['get'], 1),
    (['hosts'], ['get', 'patch'], 2),
    (['health'], ['get'], 1),
    (['sensors'], ['get'], 1),
    (['system', 'info'], ['get'], 1),
    (['search'], ['get'], 2),
    (['threat_feeds'], ['get', 'post'], 2),
    (['proxies'], ['get', 'post', 'patch'], 2),
    (['tagging'], ['get', 'patch'], 2),
])
def test_supported_endpoints(mocker, attrs, methods, version):
    """Test endpoint methods and versions.

    Test that all endpoints can be reached as attributes.
    """
    mocker.patch('requests.request')

    client = get_client(version)

    for method in methods:
        endpoint = client
        for attr in attrs:
            endpoint = getattr(endpoint, attr)
        assert getattr(endpoint, method)()
        assert requests.request.called, 'requests was not called'
        requests.request.reset_mock()


@pytest.mark.parametrize('version', [1, 2])
def test_api_validator(mocker, version):
    """Test api validator.

    For each version of the client, test at least one endpoint that is not supported.

    GET /search is not available on v1
    GET /settings is not available on v2
    """
    mocker.patch('requests.request')
    client = get_client(version)

    with pytest.raises(NotImplementedError):
        client.search.get()
        client.settings.get()
