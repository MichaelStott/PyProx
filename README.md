# PyProx

Scrapes https://www.us-proxy.org/ for list of active proxies. Useful for web scraping.

### Demo
```python
from pyprox import PyProx
import requests

# Get list of proxies.
pyprox = PyProx()
pyprox.update_proxy_list()

# Choose a random proxy from the list for the request. See the source code
# for more information.
with requests.Session() as s:
    r = s.get("https://www.google.com",
              proxies=pyprox.get_random_proxy({"https":"yes",
                                               "anonymity":"anonymous"})
    print r.text
```


