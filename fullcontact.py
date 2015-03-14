# -*- coding: UTF-8 -*-

__author__ = 'Amer Almadani (Mad_Dev)'
import requests
import json


class FullContact(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://api.fullcontact.com/v2/'
        self.person = 'person.json'
        self.disposable = 'email/disposable.json'
        self.name_normalizer = 'name/normalizer.json'
        self.name_deducer = 'name/deducer.json'
        self.name_similarity = 'name/similarity.json'
        self.name_stats = 'name/stats.json'
        self.name_parser = 'name/parser.json'
        self.address_locationNormalizer = 'address/locationNormalizer.json'
        self.address_locationEnrichment = 'address/locationEnrichment.json'
        self.batch = 'batch.json'

    def call(self, param):
        """
        Contains dict. Returns uri from __init__.

        @param :: name of call :: str

        Returns

        FullCall :: https://api.fullcontact.com/v2/+call[param]
        Call :: call[param]

        """
        call = {
            'person': self.person,
            'disposable': self.disposable,
            'normalizer': self.name_normalizer,
            'deducer': self.name_deducer,
            'similarity': self.name_similarity,
            'stats': self.name_stats,
            'parser': self.name_parser,
            'locationNormalizer': self.address_locationNormalizer,
            'locationEnrichment': self.address_locationEnrichment,
            'batch': self.batch
        }

        out = {
            'FullCall': self.url + call[param],
            'Call': call[param]
        }

        return out

    def get(self, param, **kwargs):
        """
        Create a GET request for indiviual calls

        @param :: FullCall of desired request (person for person.json) :: str
        @kwargs :: As per API docs

        """
        if 'apiKey' not in kwargs:
            kwargs['apiKey'] = self.api_key
        r = requests.get(self.call(param)['FullCall'], params=kwargs)

        return json.loads(r.text)

    def make_url(self, param, *kwargs):
        """
        Create a url for batch calls.

        @param :: FullCall of desired request (person for person.json) :: str
        @kwargs :: param=value :: tuple

        """

        return self.call(param)['FullCall'] + '?' + kwargs[0]

    def post_batch(self, batch_order):
        """
        Create a POST request for batch calls

        @batch_order :: list of makeUrl's :: list

        """
        h = {'content-type': 'application/json'}
        data = {'requests': batch_order}
        param = {'apiKey': self.api_key}
        r = requests.post(self.call('batch')['FullCall'], params=param, data=json.dumps(data), headers=h)

        return json.loads(r.text)
