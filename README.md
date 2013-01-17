# FullContact.py

A simple Python interface for [FullContact](http://www.fullcontact.com/), using Requests.

# Install

In terminal:

    pip install git+https://github.com/garbados/fullcontact.py.git

# Usage

In your Python script:

    from fullcontact import FullContact

    fc = FullContact('your_api_key')
    person_profile = fc.get(email='you@email.com')

# FullContact API Documentation

Check out FullContact's documentation [here](http://www.fullcontact.com/developer/docs/).

# Tests

To run the test suite, go to whatever directory the project is in, and:

    python setup.py test

You'll be prompted for an API key. Enter a valid one, and all the tests will (as of this writing) pass.