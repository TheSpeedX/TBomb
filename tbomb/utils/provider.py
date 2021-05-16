import threading
import requests
import json
import time
from pkg_resources import resource_string


class APIProvider:

    api_providers = []
    delay = 0
    status = True

    def __init__(self, cc, target, mode, delay=0):
        try:
            PROVIDERS = requests.get(
                "https://github.com/TheSpeedX/TBomb/raw/master/apidata.json"
            ).json()
        except Exception:
            PROVIDERS = json.loads(
                resource_string(__name__, 'apidata.json').decode())
        self.config = None
        self.cc = cc
        self.target = target
        self.mode = mode
        self.index = 0
        self.lock = threading.Lock()
        self.api_version = PROVIDERS.get("version", "2")
        APIProvider.delay = delay
        providers = PROVIDERS.get(mode.lower(), {})
        APIProvider.api_providers = providers.get(cc, [])
        if len(APIProvider.api_providers) < 10:
            APIProvider.api_providers += providers.get("multi", [])

    def format(self):
        config_dump = json.dumps(self.config)
        config_dump = config_dump.replace("{target}", self.target)
        config_dump = config_dump.replace("{cc}", self.cc)
        self.config = json.loads(config_dump)

    def select_api(self):
        try:
            if len(APIProvider.api_providers) == 0:
                raise IndexError
            self.index += 1
            if self.index >= len(APIProvider.api_providers):
                self.index = 0
        except IndexError:
            self.index = -1
            return
        self.config = APIProvider.api_providers[self.index]
        perma_headers = {"User-Agent":
                         "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)"
                         " Gecko/20100101 Firefox/72.0"}
        if "headers" in self.config:
            self.config["headers"].update(perma_headers)
        else:
            self.config["headers"] = perma_headers
        self.format()

    def remove(self):
        try:
            del APIProvider.api_providers[self.index]
            return True
        except Exception:
            return False

    def request(self):
        self.select_api()
        if not self.config or self.index == -1:
            return None
        identifier = self.config.pop("identifier", "").lower()
        del self.config['name']
        self.config['timeout'] = 30
        response = requests.request(**self.config)
        return identifier in response.text.lower()

    def hit(self):
        try:
            if not APIProvider.status:
                return
            time.sleep(APIProvider.delay)
            self.lock.acquire()
            response = self.request()
            if response is False:
                self.remove()
            elif response is None:
                APIProvider.status = False
            return response
        except Exception:
            response = False
        finally:
            self.lock.release()
            return response
