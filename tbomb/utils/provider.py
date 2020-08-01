import requests
import json
import random
import threading

class APIProvider:

    api_providers=[]

    def __init__(self,cc,target,mode):    
        with open('apidata.json', 'r') as file:
            PROVIDERS = json.load(file)
        self.config = None
        self.cc = cc
        self.target = target
        self.mode = mode
        self.index = 0
        self.lock = threading.Lock()
        providers=PROVIDERS.get(mode.lower(),{})
        if (mode.lower()=="mail"):
            APIProvider.api_providers = providers.get("mail",[])
        else:
            APIProvider.api_providers = providers.get(cc,providers.get("multi",[]))

    def format(self):
        config_dump = json.dumps(self.config)
        config_dump = config_dump.replace("{target}",self.target).replace("{cc}",self.cc)
        self.config = json.loads(config_dump)

    def select_api(self):
        try:
            self.index = random.choice(range(len(APIProvider.api_providers)))
        except IndexError:
            self.index=-1
        self.config = APIProvider.api_providers[self.index]
        perma_headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"}
        if "headers" in self.config:
            self.config["headers"].update(perma_headers)
        else:
            self.config["headers"]=perma_headers
        self.format()

    def remove(self):
        try:
            del APIProvider.api_providers[self.index]
            return True
        except:
            return False

    def request(self):
        self.select_api()
        if not self.config or self.index==-1:
            return None
        identifier=self.config.pop("identifier","").lower()
        del self.config['name']
        self.config['timeout']=30
        response=requests.request(**self.config)
        return identifier in response.text.lower()

    def hit(self):
        try:
            self.lock.acquire()
            response = self.request()
            if response==False:
                self.remove()
            return response
        except:
            response=False
        finally:
            self.lock.release()
            return response
