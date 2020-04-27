import requests


class Proxier:
    API = "api.proxier.io"
    PROXY_ENDPOINT = "proxy"

    def __init__(self):
        self.ip = None
        self.port = None

    def get(self):
        response = requests.get("https://{}/{}".format(self.API, self.PROXY_ENDPOINT))
        if response.status_code == 200:
            data = response.json()
            for prop in ("ip", "port"):
                setattr(self, prop, data.get(prop))
        return self.ip, self.port




