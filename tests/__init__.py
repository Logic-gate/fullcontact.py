from fullcontact import FullContact
import json
from attest import Tests, assert_hook

fc_tests = Tests()
api_key = raw_input("Please enter an API key for FullContact: ")
fc = FullContact(api_key)
test_email = "garbados@gmail.com"
test_twitter = "garbados"

@fc_tests.test
def bad_key():
    test = fc.get(email=test_email, apiKey='this is a bad api key')
    assert test['status'] == 403

@fc_tests.test
def bad_params():
    test = fc.get()
    assert test['status'] == 422

@fc_tests.test
def good_param():
    test = fc.get(email=test_email)
    assert test['status'] == 200

@fc_tests.test
def many_params():
    test = fc.get(email=test_email, twitter=test_twitter)
    assert test['status'] == 200

