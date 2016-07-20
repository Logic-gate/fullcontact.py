from types import FunctionType
from fullcontact import FullContact
from nose.tools import assert_equal, assert_true


class TestFullContact(object):
    def test_init(self):
        fc = FullContact('test_key')
        assert_equal(fc.api_key, 'test_key')

    def test__prepare_batch_url(self):
        fc = FullContact('test_key')
        assert_equal(
            fc._prepare_batch_url(('person', {'email': 'test@test.com'})),
            'https://api.fullcontact.com/v2/person.json?email=test%40test.com'
        )

    def test_invalid_api_keys(self):
        fc = FullContact('test_key')
        r = fc.person(email='test@test.com')
        assert_equal(r.status_code, 403)

        test_batch = [
            ('person', {'email': 'potato@yam.foo'}),
            ('person', {'name': 'Bob Smith'})
        ]

        r = fc.api_batch(test_batch)
        assert_equal(r.status_code, 403)

    def test_adds_endpoint_methods(self):
        fc = FullContact('')
        for endpoint in fc.get_endpoints:
            assert_true(isinstance(getattr(fc, endpoint), FunctionType))
