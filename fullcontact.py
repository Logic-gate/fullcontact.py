# -*- coding: UTF-8 -*-

import requests
import json


class FullContact(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.fullcontact.com/v2/'
        self.get_endpoints = {
            'person': 'person.json',
            'disposable': 'email/disposable.json',
            'name_normalizer': 'name/normalizer.json',
            'name_deducer': 'name/deducer.json',
            'name_similarity': 'name/similarity.json',
            'name_stats': 'name/stats.json',
            'name_parser': 'name/parser.json',
            'address_locationNormalizer': 'address/locationNormalizer.json',
            'address_locationEnrichment': 'address/locationEnrichment.json'
        }
        self.post_endpoints = {
            'batch': 'batch.json'
        }

    def make_url(self, endpoint):
        return self.base_url + self.get_endpoints[endpoint]

    def api_get(self, endpoint, **kwargs):
        kwargs['apiKey'] = self.api_key  # always include API key
        return requests.get(self.make_url(endpoint), params=kwargs)

    def prepare_batch_url(self, b):
        import urllib
        return self.base_url + self.get_endpoints[b['endpoint']] + urllib.urlencode(b['url_params'])

    def api_batch(self, batch_calls):
        payload = [self.prepare_batch_url(b) for b in batch_calls]
        h = {'content-type': 'application/json'}
        data = {'requests': payload}
        param = {'apiKey': self.api_key}
        r = requests.post(self.post_endpoints['batch'], params=param, data=json.dumps(data), headers=h)
