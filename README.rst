=================
Vectra API Client
=================


.. image:: https://img.shields.io/pypi/v/vectra-api-client.svg
        :target: https://pypi.python.org/pypi/vectra-api-client

.. image:: https://img.shields.io/travis/vicyap/vectra-api-client.svg
        :target: https://travis-ci.org/vicyap/vectra-api-client

.. image:: https://readthedocs.org/projects/vectra-api-client/badge/?version=latest
        :target: https://vectra-api-client.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Vectra API Client


* Free software: MIT license
* Documentation: https://vectra-api-client.readthedocs.io.


Overview
--------

This project is a Vectra Detect API Client written with a focus on python. It uses
https://swagger.io in order to automatically generate the low-level api objects. From
there, it aims to provide a thin convenience wrapper around those apis.

Since this project uses swagger, a client library in any language should be possible to
generate. I hope this helps helps increase accessibility and ease of use.


Usage
-----

**Get Detections (v1)**
```
from vectra_api_client import apis
username = 'vectra'
password = 'password'
host = 'https://vectra-ip-or-hostname.com'
api = apis.v1(host, username, password)
query_params = {
    'type_vname': 'data smuggler',
    'src_ip': '172.16.106.116',
}
detections = api.detections_get(**query_params)

```

**Get Detections (v2)**
```
from vectra_api_client import apis
token = 'TokenFromProfilePage'
host = 'https://vectra-ip-or-hostname.com'
api = apis.v2(host, token)
query_params = {
    'src_ip': '172.16.106.116',
    'threat_gte': 50,
}
detections = api.detections_get(**query_params)

```

**Get Hosts (v1)**
```
from vectra_api_client import apis
username = 'vectra'
password = 'password'
host = 'https://vectra-ip-or-hostname.com'
api = apis.v1(host, username, password)
query_params = {
    'state': 'active',
    'name': 'tb5-7',
}
api.hosts_get(**query_params)

```

**Get Hosts (v2)**
```
from vectra_api_client import apis
token = 'TokenFromProfilePage'
host = 'https://vectra-ip-or-hostname.com'
api = apis.v2(host, username, password)
query_params = {
    'state': 'active',
    'name': 'tb5-7',
}
api.hosts_get(**query_params)


```

**Search (v2)**
```
from vectra_api_client import apis
token = 'TokenFromProfilePage'
host = 'https://vectra-ip-or-hostname.com'
api = apis.v2(host, username, password)
query_string = 'host.threat:>=50 and host.certainty:>=50'
hosts = api.search_hosts_get(query_string=query_string)

```

**System Info (v1)**
```
from vectra_api_client import apis
username = 'vectra'
password = 'password'
host = 'https://vectra-ip-or-hostname.com'
api = apis.v1(host, username, password)
system_info = api.system_info_get()

```

**Other Endpoints**

The api objects returned from `apis.(v1|v2)` have a `.session` attribute
that allow you to hit any endpoint under their respective base url api routes.
(eg. v1 will use /api as the base url and v2 will use /api/v2 as the base url.)
This `.session` attribute is from http://docs.python-requests.org/en/master/user/advanced/#session-objects

```
# v1
from vectra_api_client import apis
username = 'vectra'
password = 'password'
host = 'https://vectra-ip-or-hostname.com'
api = apis.v1(host, username, password)
api.session.get('endpoint/under/development')  # GET {host}/api/endpoint/under/development
api.session.post('endpoint/under/development')  # POST {host}/api/endpoint/under/development

# v2
from vectra_api_client import apis
token = 'TokenFromProfilePage'
host = 'https://vectra-ip-or-hostname.com'
api = apis.v1(host, username, password)
api.session.get('endpoint/under/development')  # GET {host}/api/v2/endpoint/under/development
api.session.post('endpoint/under/development')  # POST {host}/api/v2/endpoint/under/development

```

Installation
------------

* (python) `pip install vectra-api-client`

Other Languages
~~~~~~~~~~~~~~~

`GENERATOR_NAME=$lang OUTPUT_DIR=output make swagger`


Contributing
------------

All contributions to the project are welcome! Fork the repo and make a PR.
Making github issues is also completely fine as well.

Developing
~~~~~~~~~~

* docker is required. It is used to run openapi/openapi-generator-cli

```
pip install -r requirements.txt
pip install -r requirements_dev.txt
make swagger
make test
make test-all

```

TODO
----

API v1
~~~~~~

[] /settings
[] /rules
[x] /detections
[x] /hosts
[] /health
[] /sensors
[x] /system/info


API v2
~~~~~~

[] /rules
[x] /detections
[] /hosts
[x] /search
[x] /threatFeeds
[x] /proxies
[] /tagging


This project uses https://swagger.io/ in order to generate its low-level http api classes.

Resources
---------

* https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Thanks to Moosh for his early contributions.
