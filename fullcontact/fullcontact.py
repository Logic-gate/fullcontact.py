import json
import logging
import requests
import urllib


log = logging.getLogger(__name__)


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

    def api_get(self, endpoint, strict=False, **kwargs):
        """ Makes a FullContact API call

        Formats and submits a request to the specified endpoint, appending
        any key-value pairs passed in kwargs as a url query parameter.

        Args:
            endpoint: shortname of the API endpoint to use.
            strict: if True, throw an error
            **kwargs: a dict of query parameters to append to the request.

        Returns:
            A Requests object containing the result of the API call. Interact
            with the return value of this function as you would with any
            other Requests object.

        Raises:
            KeyError: the specified endpoint was not recognized. Check the
                docs.
            Requests.Exceptions.*: an error was raised by the Requests
                module.
        """

        kwargs['apiKey'] = self.api_key  # always include API key
        r = requests.get(self.base_url + self.get_endpoints[endpoint], params=kwargs)

        return r


    def _prepare_batch_url(self, b):
        """ Format a url to submit to the batch API

        Args:
            b: a tuple of (str, dict) containing the endpoint for
                the request and a dict of url parameters (note:
                the api key doesn't need to be included for
                individual requests within a batch since it is
                appended to the batch API call.

        Returns:
            A formatted url to append to the batch request's payload.
        """
        batch_url = self.base_url + self.get_endpoints[b[0]] + '?' + urllib.urlencode(b[1])
        log.debug('Prepared batch url: {}'.format(batch_url))

        return batch_url

    def api_batch(self, batch_calls):
        payload = [self._prepare_batch_url(b) for b in batch_calls]
        h = {'content-type': 'application/json'}
        data = {'requests': payload}
        param = {'apiKey': self.api_key}
        full_endpoint = self.base_url + self.post_endpoints['batch']

        r = requests.post(full_endpoint, params=param, data=json.dumps(data), headers=h)

        return r
