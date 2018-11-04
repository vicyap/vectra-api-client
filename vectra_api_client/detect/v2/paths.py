"""Detect API v2 Paths."""

class RulesPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /rules"""
        return self.client.request('GET', '/rules').json()

    def post(self):
        """POST /rules"""
        return self.client.request('POST', '/rules').json()

    def put(self):
        """PUT /rules"""
        return self.client.request('PUT', '/rules').json()

    def delete(self):
        """DELETE /rules"""
        return self.client.request('DELETE', '/rules').json()

    def options(self):
        """OPTIONS /rules"""
        return self.client.request('OPTIONS', '/rules').json()

class DetectionsPath(object):
    def __init__(self, client):
        self.client = client

    def get(self, json=False, params=None):
        """GET /detections"""
        if params is None:
            params = {}
        resp = self.client.request('GET', '/detections', params=params)
        if json:
            return resp.json()
        return resp

    def patch(self):
        """PATCH /detections"""
        return self.client.request('PATCH', '/detections').json()

class HostsPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /hosts"""
        return self.client.request('GET', '/hosts').json()

    def patch(self):
        """PATCH /detections"""
        return self.client.request('PATCH', '/detections').json()

class SearchPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /search"""
        return self.client.request('GET', '/search').json()

class ThreatFeedsPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /threatFeeds"""
        return self.client.request('GET', '/threatFeeds').json()

    def post(self):
        """POST /threadFeeds"""
        return self.client.request('POST', '/threatFeeds').json()

class ProxiesPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /proxies"""
        return self.client.request('GET', '/proxies').json()

    def post(self):
        """POST /proxies"""
        return self.client.request('POST', '/proxies').json()

    def patch(self):
        """PATCH /proxies"""
        return self.client.request('PATCH', '/proxies').json()

class TaggingPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /tagging"""
        return self.client.request('GET', '/tagging').json()

    def patch(self):
        """PATCH /tagging"""
        return self.client.request('PATCH', '/tagging').json()

