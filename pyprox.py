import lxml.html
import random
import requests


class PyProx():
    """ Scrapes us-proxy.org for list of proxies. Useful for web scraping.
    """
    
    DOMAIN = "https://www.us-proxy.org/"

    def __init__(self):
        self.proxies = []
        
    def update_proxy_list(self, anonymity=""):
        with requests.Session() as s:
            r = s.get(self.DOMAIN)
            root = lxml.html.fromstring(r.text)
            table = root.xpath("//tbody/tr")
            for row in table:
                properties = row.xpath("td/text()")
                self.proxies.append({
                        "ip_addr":properties[0],
                        "port":properties[1],
                        "code":properties[2],
                        "country":properties[3],
                        "anonymity":properties[4],
                        "google":properties[5],
                        "https":properties[6],
                        "last_checked":properties[7]
                    })

    def get_random_proxy(self, options={}):
        if not options:
            return random.choice(self.proxies)
        filter_prox = []
        for proxy in self.proxies:
            if all(item in proxy.items() for item in options.items()):
               filter_prox.append(proxy)
        return random.choice(filter_prox)

    def can_proxy_connect(self, proxy, domain=""):
        # NOTE: If this function returns false, it may not necessarily
        # indicate that the proxy is inactive. The request may have been
        # rejected if the server detects that it did not originate from
        # a browser.
        if not domain:
            domain = "https://www.google.com/"
        with requests.Session() as s:
            try:
                r = s.get(domain, proxies={"http": "http://" +
                                           proxy["ip_addr"]})
                return r.status_code < 400
            except:
                return False
            
            
if __name__ == "__main__":
    pyprox = PyProx()
    pyprox.update_proxy_list()
    proxy = pyprox.get_random_proxy(options={"https":"yes",
                                             "anonymity":"anonymous"})
    print pyprox.can_proxy_connect(proxy)
    
    
