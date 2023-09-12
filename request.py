from typing import Dict
import requests
from time import sleep
import json


class client():
    def __init__(self, IP, schema, timeout = 5) -> None:
        self.IP = IP
        self.timeout = timeout
        f = open(schema)
        JSON = json.load(f)
        self.funct = {}
        for x in JSON:
            name = x.get('name')
            method = x.get('type')
            endpt = x.get('endpoint')
            parameters = x.get('parameters')

            self.funct[name] = [method,endpt,parameters]
        pass

    def load(self, name):
        # fn = lambda **kwargs: print(kwargs)
        for x in self.funct:
            if name == x:
                method: str = self.funct[x][0]
                endpt: str = self.funct[x][1]
                parameters: list = self.funct[x][2]
                if method == "get":
                    fn = lambda **kwargs: self.get(endpt, kwargs, parameters)
                
                elif method == "post":
                    fn = lambda **kwargs: self.post(endpt, kwargs, parameters)

        return fn

    def get(self, endpoint, kwargs, parameters=None):
        req = "http://" + self.IP + endpoint

        params = None
        if parameters is not None:
            params = {}
            for param in parameters:
                params[param] = kwargs[param]
        
        res = requests.get(req,
                           timeout=self.timeout,
                           params=params)
        response = float(res.text)

        return response
    
    def post(self, endpoint, kwargs, parameters=None):
        req = "http://" + self.IP + endpoint

        params = None
        if parameters is not None:
            params = {}
            for param in parameters:
                params[param] = kwargs[param]

        res = requests.post(req,
                           timeout=self.timeout,
                           params=params)

        return None
    

    def __call__(self, fn: str, **kwargs):
        return self.load(fn)(**kwargs)

exp = client("0.0.0.0",'requests.json')
print(exp("set_dac_sampling_rate", rate = 0))

