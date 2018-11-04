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
    attach_session_to(s, api)

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
    attach_session_to(s, api)

    return api


def attach_session_to(session, attach_to):
    s = session
    attach_to.session = s
    attach_to.get = s.get
    attach_to.head = s.get
    attach_to.post = s.post
    attach_to.put = s.put
    attach_to.delete = s.delete
    attach_to.patch = s.patch
    attach_to.options = s.options


def PrefixUrlSession(prefix):
    prefix = prefix.rstrip('/') + '/'

    def new_request(prefix, f, method, url, *args, **kwargs):
        return f(method, prefix + url, *args, **kwargs)

    s = requests.Session()
    s.request = partial(new_request, prefix, s.request)
    return s
