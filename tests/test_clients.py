#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `vectra_api_client` package."""

import pytest
import requests


from vectra_api_client import clients


def test_clients_v1(mocker):
    mocker.patch('requests.request')

    client = clients.DetectClientV1(host='', username='', password='')
    client.request('GET', '/whatever')
    assert requests.request.called


def test_clients_v2(mocker):
    mocker.patch('requests.request')

    client = clients.DetectClientV2(host='', token='')
    client.request('GET', '/whatever')
    assert requests.request.called
