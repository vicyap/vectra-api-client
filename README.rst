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
