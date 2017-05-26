# PyProx

Scrapes https://www.us-proxy.org/ for list of active proxies. Useful for web scraping.

### Demo
```python
from pyprox import PyProx
import requests
pyprox = PyProx()
pyprox.update_proxy_list()
with requests.Session() as s:
    r = s.get("https://www.google.com",
              proxies=pyprox.get_random_proxy({"https":"yes",
                                               "anonymity":"anonymous"})
    print r.text
```


