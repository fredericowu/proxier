from . import proxier
from functools import partial
from requests.exceptions import ProxyError, ConnectTimeout, ReadTimeout
import requests


def request_function(func, *args, **kwargs):
    proxy_url = "http://{}:{}".format(*proxier.get(force_new=kwargs.pop("_proxier_force_new", False)))
    kwargs["proxies"] = {
        "http": proxy_url,
        "https": proxy_url
    }
    try:
        return func(*args, **kwargs)
    except (ProxyError, ConnectTimeout, ReadTimeout):
        kwargs["_proxier_force_new"] = True
        return request_function(func, *args, **kwargs)


get = partial(request_function, requests.get)
delete = partial(request_function, requests.delete)
post = partial(request_function, requests.post)
put = partial(request_function, requests.put)
