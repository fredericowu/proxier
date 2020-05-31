import requests


class Proxier:
    API_HOST = "api.proxier.io"
    PROXY_ENDPOINT = "proxy"

    def __init__(self):
        self.ip = None
        self.port = None

    def get(self):
        response = requests.get("https://{}/{}".format(self.API_HOST, self.PROXY_ENDPOINT))
        if response.status_code == 200:
            data = response.json()[0]
            for attr in ("ip", "port"):
                setattr(self, attr, data.get(attr))
        return self.ip, self.port


proxier = Proxier()


def get_proxy():
    return proxier.get()


def get_requests_proxy():
    ip, port = proxier.get()
    result = {
        "http": "http://{}:{}".format(ip, port)
    }
    return result





