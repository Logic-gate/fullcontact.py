# FullContact.py

A simple Python interface for [FullContact](http://www.fullcontact.com/), using Requests.

# Install

In terminal:

    pip install fullcontact.py

# Usage

In your Python script:

    from fullcontact import FullContact

    fc = FullContact('your_api_key')
    person_profile = f.get('person', email='you@email.com')
    
    '''
	'person'
    'disposable'
    'normalizer' 
    'deducer'
    'similarity'
    'stats'
    'parser' 
    'locationNormalizer'
    'locationEnrichment'
    'batch'
    '''
    #for batch
    
    fc = FullContact('your_api_key')
	batch_order = [f.makeUrl('person', 'email=you@email.com'), f.makeUrl('normalizer','q=Your name')]
	f.postBatch(batch_order)

# FullContact API Documentation

Check out FullContact's documentation [here](http://www.fullcontact.com/developer/docs/).

# Tests

To run the test suite:

    git clone git://github.com/garbados/fullcontact.py.git
    cd fullcontact.py
    python setup.py test

You'll be prompted for an API key. Enter a valid one, and all the tests will (as of this writing) pass.
