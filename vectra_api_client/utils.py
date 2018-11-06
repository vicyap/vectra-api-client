"""Utils."""

from functools import partial
import requests


def proxy_attr(proxy, real, attr):
    """Proxy attr from `real.attr` to `proxy.attr`.

    >>> real = type('real', (), {})
    >>> real.session = type('session', (), {})
    >>> real.session.get = 'get'

    >>> proxy = type('proxy', (), {})
    >>> proxy_attr(proxy, real.session, 'get')

    >>> assert proxy.get == real.session.get
    """
    setattr(proxy, attr, getattr(real, attr))


def proxy_attrs(proxy, real, attrs):
    """Proxy multiple attrs using proxy_attr

    >>> attrs = ['get', 'post', 'delete']

    >>> real = type('real', (), {})
    >>> real.session = type('session', (), {})
    >>> for attr in attrs:
    ...     setattr(real.session, attr, attr)

    >>> proxy = type('proxy', (), {})
    >>> proxy_attrs(proxy, real.session, attrs)

    >>> for attr in attrs:
    ...     assert getattr(proxy, attr) == getattr(real.session, attr)
    """
    for attr in attrs:
        proxy_attr(proxy, real, attr)


def PrefixUrlSession(prefix):
    def new_request(prefix, f, method, url, *args, **kwargs):
        return f(method, prefix + url, *args, **kwargs)

    s = requests.Session()
    s.request = partial(new_request, prefix.rstrip('/') + '/', s.request)
    return s
