import requests


class Proxier:
    API_HOST = "api.proxier.io"
    PROXY_ENDPOINT = "proxy"
    _proxy_list = []
    LIST_COUNT = 7

    def __init__(self):
        self.proxy = None
        self.country_name = None

    def set_country_name(self, name):
        self.country_name = name

    def unset_country_name(self):
        self.country_name = None

    def get_ip_port(self):
        return self.proxy.get("ip"), self.proxy.get("port")

    def has_ip_port(self):
        return self.proxy and self.proxy.get("ip") and self.proxy.get("port")

    def get_next(self, retry=0):
        try:
            self.proxy = Proxier._proxy_list.pop()
            while self.proxy.get("is_https") == "no":
                self.proxy = Proxier._proxy_list.pop()
        except IndexError:
            if retry == 5:
                raise Exception("Retrieving list error")
            self.retrieve_list()
            return self.get_next(retry+1)
        return self.get_ip_port()

    def get(self, force_new=False):
        if force_new or not self.has_ip_port():
            return self.get_next()
        return self.get_ip_port()

    def retrieve_list(self):
        params = {
            "count": Proxier.LIST_COUNT
        }
        if self.country_name:
            params["country_name"] = self.country_name
        response = requests.get("https://{}/{}".format(self.API_HOST, self.PROXY_ENDPOINT), params=params)
        if response.status_code == 200:
            self._proxy_list += response.json()
        else:
            raise Exception("Error retrieving the proxy list status code: {}".format(response.status_code))


proxier = Proxier()


def get_proxy():
    return proxier.get()


def get_requests_proxy():
    ip, port = proxier.get()
    result = {
        "http": "http://{}:{}".format(ip, port)
    }
    return result





