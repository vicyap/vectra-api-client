# -*- coding: utf-8 -*-

"""Clients module."""
import requests

from vectra_api_client import detect
import detect.v1
import detect.v1.paths
import detect.v2
import detect.v2.paths


class DetectClientV1(object):
    def __init__(self, url=None, username=None, password=None, verify=True):
        self.url = url + '/api'
        self.verify = verify
        self.auth = (username, password)

        # self.settings = detect.path.v1.SettingsPath(self)
        # self.rules = detect.path.v1.RulesPath(self)
        self.detections = detect.path.v1.DetectionsPath(self)  # client.detections.get()
        # self.hosts = detect.path.v1.HostsPath(self)



        self.health = detect.path.v1.HealthPath(self)
        # client.health.get()
        # client.health.subnets.get()
        # client.health.traffic.get()
        # client.health.headend(brain_luid).get()
        # client.health.headend(brain_luid).subnets.get(params={}, raw_response=True)



        # self.sensors = detect.path.v1.SensorsPath(self)
        # self.system = detect.path.v1.SystemPath(self)
        # client.system.info.get()

    def request(self, method, path, **kwargs):
        """Allows requests to any endpoint."""
        new_kwargs = {
            'verify': self.verify,
            'auth': self.auth,
        }
        new_kwargs.update(kwargs)  # override default values with kwargs parameter
        return requests.request(method, self.url + path, **new_kwargs)

    def get_token(self, create=False):
        """Get the API v2 token.

        Args:
            create (bool): create the token if one does not exist.
        """
        raise NotImplementedError()


class DetectClientV2(object):
    def __init__(self, url=None, token=None, verify=True):
        self.url = url + '/api/v2'
        self.token = token
        self.verify = verify
        self.headers = {
            'Authorization': 'Token ' + token.strip()
        }

        self.rules = detect.v2.paths.RulesPath(self)
        self.detections = detect.v2.paths.DetectionsPath(self)
        self.hosts = detect.v2.paths.HostsPath(self)
        self.search = detect.v2.paths.SearchPath(self)
        self.threat_feeds = detect.v2.paths.ThreatFeedsPath(self)
        self.proxies = detect.v2.paths.ProxiesPath(self)
        self.tagging = detect.v2.paths.TaggingPath(self)

    def request(self, method, path, **kwargs):
        """Allows requests to any endpoint."""
        new_kwargs = {
            'verify': self.verify,
            'headers': self.headers,
        }
        new_kwargs.update(kwargs)  # override default values with kwargs parameter
        return requests.request(method, self.url + path, **new_kwargs)

    def regen_token(self):
        """Regenerate the API v2 token."""
        raise NotImplementedError()
