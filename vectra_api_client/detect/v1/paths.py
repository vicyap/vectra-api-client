"""Detect API v1 Paths"""

from vectra_api_client.detect.v1 import responses


class SystemPath(object):
    def __init__(self, client):
        self.client = client
        self.info = SystemPath.Info(self.client)

    class Info(object):
        def __init__(self, client):
            self.client = client

        def get(self):
            """GET /system/info"""
            return self.client.request('GET', '/system/info').json()

class SettingsPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /settings"""
        return self.client.request('GET', '/settings').json()

class RulesPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /rules"""
        return self.client.request('GET', '/rules').json()


    def get(client, raw=False, params=None):
        """GET /detections

        Args:
            raw (bool): if True, return the requests response instead of an object
            params (dict): a dictionary of params to pass to the request
        """
        if params is None:
            params = {}
        resp = client.request('GET', '/detections', params=params)
        if raw:
            return resp
        return responses.DetectionsGET.from_dict(resp.json())

class HostsPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /hosts"""
        return self.client.request('GET', '/hosts').json()


class HealthPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /health"""
        return self.client.request('GET', '/health').json()

    @property
    def subnets(self):
        return HealthPath.SubnetsPath(self.client)

    def headend(self, brain_luid):
        """GET /health/headend/<brain_luid>"""
        return HealthPath.HeadendPath(self.client, brain_luid)

    @property
    def subnet_counts(self):
        return HealthPath.SubnetCountsPath(self.client)

    @property
    def traffic(self):
        return HealthPath.TrafficPath(self.client)

    class SubnetsPath(object):
        def __init__(self, client):
            self.client =client

        def get(self):
            """GET /health/subnets"""
            return self.client.request('GET', '/health/subnets').json()

    class HeadendPath(object):
        def __init__(self, client, brain_luid):
            self.client = client
            self.brain_luid = brain_luid

            self.subnets = HealthPath.HeadendPath.SubnetsPath(self.client)

        def get(self):
            """GET /health/headend/<brain_luid>"""
            return self.client.request('GET', '/health/headend/{}'.format(brain_luid)).json()

        class SubnetsPath(object):
            def __init__(self, client, brain_luid):
                self.client = client
                self.brain_luid

            def get(self):
                """GET /health/headend/<brain_luid>/subnets"""
                return self.client.request('GET', '/health/headend/{}/subnets'.format(self.brain_luid)).json()


class SensorsPath(object):
    def __init__(self, client):
        self.client = client

    def get(self):
        """GET /sensors"""
        return self.client.request('GET', '/sensors').json()
