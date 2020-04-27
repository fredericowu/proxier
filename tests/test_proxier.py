# -*- encoding: utf-8
from proxier import Proxier
import requests_mock


def test_proxier_get(mocker):
    with requests_mock.Mocker() as mock_request:
        mock_request.get("https://api.proxier.io/proxy", json={'ip': '127.0.0.1', 'port': 8080})
        ip, port = Proxier().get()

        assert ip == '127.0.0.1'
        assert port == 8080
