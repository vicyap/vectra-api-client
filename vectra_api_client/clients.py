# -*- coding: utf-8 -*-

"""Clients module."""

import functools
import requests


def api(*args):
    def decorator(f):
        @functools.wraps(f)
        def inner(self, **kwargs):
            if self.client.version in args:
                return f(self, **kwargs)
            else:
                raise NotImplementedError('Method unsupport on version {}'.format(self.client.version))
        return inner
    return decorator


class DetectClient(object):
    def __init__(self, url=None, token=None, username=None, password=None, verify=True):
        self.url = url
        self.verify = verify

        if token is None:
            self.version = 1
            self.url = self.url + '/api'
            self.auth = (username, password)
        elif username is None and password is None:
            self.version = 2
            self.url = self.url + '/api/v2'
            self.headers = {
                'Authorization': 'Token ' + token.strip()
            }
        else:
            raise RuntimeError(
                'At least one form of authentication is required. Please provide a token or username and password'
            )

        self.settings = DetectClient.Settings(self)
        self.rules = DetectClient.Rules(self)
        self.detections = DetectClient.Detections(self)
        self.hosts = DetectClient.Hosts(self)
        self.health = DetectClient.Health(self)
        self.sensors = DetectClient.Sensors(self)
        self.system = DetectClient.System(self)
        self.search = DetectClient.Search(self)
        self.threat_feeds = DetectClient.ThreatFeeds(self)
        self.proxies = DetectClient.Proxies(self)
        self.tagging = DetectClient.Tagging(self)

    def request(self, method, path, **kwargs):
        """Allows requests to any endpoint."""
        new_kwargs = {'verify': self.verify}
        if self.version == 1:
            new_kwargs['auth'] = self.auth
        elif self.version == 2:
            new_kwargs['headers'] = self.headers
        new_kwargs.update(kwargs)  # override default values with kwargs parameter

        return requests.request(method, self.url + path, **new_kwargs)

    class System(object):
        def __init__(self, client):
            self.client = client

            self.info = DetectClient.System.Info(self.client)

        class Info(object):
            def __init__(self, client):
                self.client = client

            @api(1)
            def get(self):
                """GET /system/info"""
                return self.client.request('GET', '/system/info').json()

    class Settings(object):
        def __init__(self, client):
            self.client = client

        @api(1)
        def get(self):
            """GET /settings"""
            return self.client.request('GET', '/settings').json()

    class Rules(object):
        def __init__(self, client):
            self.client = client

        @api(1, 2)
        def get(self):
            """GET /rules"""
            return self.client.request('GET', '/rules').json()

        @api(2)
        def post(self):
            """POST /rules"""
            return self.client.request('POST', '/rules').json()

        @api(2)
        def put(self):
            """PUT /rules"""
            return self.client.request('PUT', '/rules').json()

        @api(2)
        def delete(self):
            """DELETE /rules"""
            return self.client.request('DELETE', '/rules').json()

        @api(2)
        def options(self):
            """OPTIONS /rules"""
            return self.client.request('OPTIONS', '/rules').json()

    class Detections(object):
        def __init__(self, client):
            self.client = client

        @api(1, 2)
        def get(self):
            """GET /detections"""
            return self.client.request('GET', '/detections').json()

        @api(2)
        def patch(self):
            """PATCH /detections"""
            return self.client.request('PATCH', '/detections').json()

    class Hosts(object):
        def __init__(self, client):
            self.client = client

        @api(1, 2)
        def get(self):
            """GET /hosts"""
            return self.client.request('GET', '/hosts').json()

        @api(2)
        def patch(self):
            """PATCH /detections"""
            return self.client.request('PATCH', '/detections').json()

    class Health(object):
        def __init__(self, client):
            self.client = client

        @api(1)
        def get(self):
            """GET /health"""
            return self.client.request('GET', '/health').json()

    class Sensors(object):
        def __init__(self, client):
            self.client = client

        @api(1)
        def get(self):
            """GET /sensors"""
            return self.client.request('GET', '/sensors').json()

    class Search(object):
        def __init__(self, client):
            self.client = client

        @api(2)
        def get(self):
            """GET /search"""
            return self.client.request('GET', '/search').json()

    class ThreatFeeds(object):
        def __init__(self, client):
            self.client = client

        @api(2)
        def get(self):
            """GET /threatFeeds"""
            return self.client.request('GET', '/threatFeeds').json()

        @api(2)
        def post(self):
            """POST /threadFeeds"""
            return self.client.request('POST', '/threatFeeds').json()

    class Proxies(object):
        def __init__(self, client):
            self.client = client

        @api(2)
        def get(self):
            """GET /proxies"""
            return self.client.request('GET', '/proxies').json()

        @api(2)
        def post(self):
            """POST /proxies"""
            return self.client.request('POST', '/proxies').json()

        @api(2)
        def patch(self):
            """PATCH /proxies"""
            return self.client.request('PATCH', '/proxies').json()

    class Tagging(object):
        def __init__(self, client):
            self.client = client

        @api(2)
        def get(self):
            """GET /tagging"""
            return self.client.request('GET', '/tagging').json()

        @api(2)
        def patch(self):
            """PATCH /tagging"""
            return self.client.request('PATCH', '/tagging').json()
