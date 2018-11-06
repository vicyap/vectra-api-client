"""High-level API."""

import python_vectra_cognito_detect_v1
import python_vectra_cognito_detect_v2

from . import utils


def v1(host, username, password, verify=True):
    prefix = host + '/api'

    s = utils.PrefixUrlSession(prefix)
    s.auth = (username, password)
    s.verify = verify

    config = python_vectra_cognito_detect_v1.Configuration()
    config.host = prefix
    config.username = username
    config.password = password
    config.verify_ssl = verify
    client = python_vectra_cognito_detect_v1.ApiClient(config)

    api = python_vectra_cognito_detect_v1.DefaultApi(client)
    api.session = s
    utils.proxy_attrs(api, api.session, ['get', 'post', 'put', 'delete', 'patch', 'options'])

    return api


def v2(host, token, verify=True):
    prefix = host + '/api/v2'

    s = utils.PrefixUrlSession(prefix)
    s.headers = {'Authorization': 'Token ' + token}
    s.verify = verify

    config = python_vectra_cognito_detect_v2.Configuration()
    config.host = prefix
    config.api_key['Authorization'] = 'Token ' + token
    config.verify_ssl = verify
    client = python_vectra_cognito_detect_v2.ApiClient(config)

    api = python_vectra_cognito_detect_v2.DefaultApi(client)
    api.session = s
    utils.proxy_attrs(api, api.session, ['get', 'post', 'put', 'delete', 'patch', 'options'])

    return api
