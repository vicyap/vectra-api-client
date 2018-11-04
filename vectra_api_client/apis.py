"""High-level API."""

import requests
from functools import partial

import detect_v1
import detect_v2


def v1(host, username, password, verify=True):
    prefix = host + '/api'

    s = PrefixUrlSession(prefix)
    s.auth = (username, password)
    s.verify = verify

    config = detect_v1.Configuration()
    config.host = prefix
    config.username = username
    config.password = password
    config.verify_ssl = verify
    client = detect_v1.ApiClient(config)

    api = detect_v1.DefaultApi(client)
    api.session = s
    return api


def v2(host, token, verify=True):
    prefix = host + '/api/v2'

    s = PrefixUrlSession(prefix)
    s.headers = {'Authorization': 'Token ' + token}
    s.verify = verify

    config = detect_v2.Configuration()
    config.host = prefix
    config.api_key['Authorization'] = 'Token ' + token
    config.verify_ssl = verify
    client = detect_v2.ApiClient(config)

    api = detect_v2.DefaultApi(client)
    api.session = s

    return api


def PrefixUrlSession(prefix=None):
    if prefix is None:
        prefix = ""
    else:
        prefix = prefix.rstrip('/') + '/'

    def new_request(prefix, f, method, url, *args, **kwargs):
        return f(method, prefix + url, *args, **kwargs)

    s = requests.Session()
    s.request = partial(new_request, prefix, s.request)
    return s
