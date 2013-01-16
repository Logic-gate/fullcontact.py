import requests
import json

class FullContact(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = url = "https://api.fullcontact.com/v2/person.json"
    def get(self, **kwargs):
        if 'apiKey' not in kwargs:
            kwargs['apiKey'] = self.api_key
        r = requests.get(self.url, params=kwargs)
        return json.loads(r.text)