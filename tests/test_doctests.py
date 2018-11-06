import doctest
import os
import pytest
import requests


README = os.path.join(
    os.path.pardir,
    'README.rst',
)


def test_doctest(mocker):
    mocker.patch('requests.Session.request')
    doctest.testfile(README)

