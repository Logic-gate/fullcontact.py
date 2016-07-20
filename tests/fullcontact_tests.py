from fullcontact import FullContact
from nose.tools import assert_equal


class TestFullContact(object):
    def test_trivial_pass(self):
        assert_equal(1, 1)

    def test_init(self):
        fc = FullContact('')
        assert_equal(fc.api_key, '')

    def test__prepare_batch_url(self):
        fc = FullContact('')
        assert_equal(
            fc._prepare_batch_url(('person', {'email': 'test@test.com'})),
            'https://api.fullcontact.com/v2/person.json?email=test%40test.com'
        )

    def test_invalid_api_keys(self):
        fc = FullContact('')
        r = fc.api_get('person', **{'email': 'test@test.com'})
        assert_equal(r.status_code, 403)

        test_batch = [
            ('person', {'email': 'potato@yam.foo'}),
            ('person', {'name': 'Bob Smith'})
        ]

        r = fc.api_batch(test_batch)
        assert_equal(r.status_code, 403)
