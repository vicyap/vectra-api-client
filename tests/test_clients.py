#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `vectra_api_client` package."""

import pytest
import requests


from vectra_api_client import clients


def test_clients_v1(mocker):
    mocker.patch('requests.Session.request')

    client = clients.v1(host='https://localhost', username='', password='')
    client.session.get('/whatever')
    assert requests.Session.request.called


def test_clients_v2(mocker):
    mocker.patch('requests.Session.request')

    client = clients.v2(host='https://localhost', token='')
    client.session.get('/whatever')
    assert requests.Session.request.called
