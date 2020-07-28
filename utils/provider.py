import requests
import urllib3
import json
import random

# This code was taken from https://github.com/AvinashReddy3108 and was updated a bit

DEFAULT_TIMEOUT = 30
VERIFY = True
not VERIFY and urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning)



class APIProvider:
    def __init__(self,target, cc='91',  proxy={}):
        with open('config.json', 'r') as f:
            PROVIDERS = json.load(f)['providers']
        self.api_providers=PROVIDERS.get(cc,PROVIDERS['multi'])
        self.config=None
        self.target = target
        self.proxy=proxy
        self.cc = cc

    def select_api(self):
        self.config=random.choice(self.api_providers)
        self.headers = self._headers()
        self.cookies = self._cookies()

    def _headers(self):
        tmp_headers = {
            "User-Agent":
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
        }
        if 'headers' in self.config:
            tmp_headers.update(self.config['headers'])
        return tmp_headers

    def _cookies(self):
        tmp_cookies = {}
        if 'cookies' in self.config:
            tmp_cookies.update(self.config['cookies'])
        return tmp_cookies

    def _data(self):
        tmp_data = {}
        for key, value in self.config['data'].items():
            tmp_data[key] = value.format(cc=self.cc, target=self.target)
        return tmp_data

    def _json(self):
        tmp_data = {}
        for key, value in self.config['json'].items():
            tmp_data[key] = value.format(cc=self.cc, target=self.target)
        return tmp_data

    def _params(self):
        tmp_params = {}
        if 'params' in self.config:
            for key, value in self.config['params'].items():
                tmp_params[key] = value.format(cc=self.cc, target=self.target)
        return tmp_params

    def _get(self):
        self.params = self._params()
        return requests.get(self.config['url'],
                            params=self.params,
                            headers=self.headers,
                            cookies=self.cookies,
                            timeout=DEFAULT_TIMEOUT,
                            proxies=self.proxy,
                            verify=VERIFY)

    def _post(self):
        self.data = self._data()
        if self.data=={}:
            self.data=self._json()
            return requests.post(self.config['url'],
                             json=self.data,
                             headers=self.headers,
                             cookies=self.cookies,
                             timeout=10,
                             proxies=self.proxy,
                             verify=VERIFY)
        return requests.post(self.config['url'],
                             data=self.data,
                             headers=self.headers,
                             cookies=self.cookies,
                             timeout=10,
                             proxies=self.proxy,
                             verify=VERIFY)

    def remove(self):
        try:
            self.api_providers.remove(self.config)
            return True
        except:
            return False

    def hit(self):
        self.select_api()
        if not self.config:
            return None
        if self.config['method'] == 'GET':
            self.response = self._get()
        elif self.config['method'] == 'POST':
            self.response = self._post()
        return self.config['identifier'].lower() in self.response.text.lower()
