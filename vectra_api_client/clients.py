"""High-level client."""

import requests

import detect_v1
import detect_v2


class DetectClientV1(object):
    def __init__(self, host, username, password, verify=True):
        self._configuration = detect_v1.Configuration()
        self._configuration.host = host + '/api'
        self._configuration.username = username
        self._configuration.password = password
        self._configuration.verify_ssl = verify

        self._client = detect_v1.ApiClient(self._configuration)
        self.detections = detect_v1.DetectionsApi(self._client)

    def request(self, method, resource_path, **kwargs):
        new_kwargs = {
            'auth': (self._configuration.username, self._configuration.password),
            'verify': self._configuration.verify_ssl,
        }
        new_kwargs.update(kwargs)
        return requests.request(method, self._configuration.host + resource_path, **new_kwargs)


class DetectClientV2(object):
    def __init__(self, host, token, verify=True):
        self.token = token
        self._configuration = detect_v2.Configuration()
        self._configuration.host = host + '/api/v2'
        self._configuration.api_key['Authorization'] = 'Token ' + token
        self._configuration.verify_ssl = verify

        self._client = detect_v2.ApiClient(self._configuration)
        self.detections = detect_v2.DetectionsApi(self._client)

    def request(self, method, resource_path, **kwargs):
        new_kwargs = {
            'headers': {'Authorization': 'Token ' + self.token},
            'verify': self._configuration.verify_ssl,
        }
        new_kwargs.update(kwargs)
        return requests.request(method, self._configuration.host + resource_path, **new_kwargs)
