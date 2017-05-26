# PyProx

Scrapes https://www.us-proxy.org/ for list of active proxies. Useful for web scraping.

### Demo
```python
import requests
pyprox = PyProx()
pyprox.update_proxy_list()
proxy = pyprox.get_random_proxy(options={"https":"yes",
                                         "anonymity":"anonymous"})
if (pyprox.can_proxy_connect(proxy)):
    with requests.Session() as s:
        r = s.get("https://www.google.com",
                  proxies={"http": "http://" + proxy["ip_addr"]})
        print r.text
```


