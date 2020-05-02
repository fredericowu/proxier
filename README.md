# Proxier
Proxier is a library to provide free access Proxy server's hosts as code.
Please, check https://proxier.io/.

## What does it do
It consumes data provided by `proxier.io` APIs.

## How to install?
  $ pip install proxier

## How to use it?

```python
import proxier
import requests

response = requests.get("http://bot.whatismyipaddress.com/", proxies=proxier.get_requests_proxy())
print("my ip: " + response.text)

```
