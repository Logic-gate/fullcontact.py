# FullContact.py

A simple Python interface for [FullContact](http://www.fullcontact.com/), using Requests.

# Install

In terminal:

    pip install fullcontact.py
    
Or just include the fullcontact API class in your project. It's entirely self-contained.

# Warning

Changes introduced in version 0.0.3 are not backwards compatible.

# Usage

    
    >>> from fullcontact import FullContact
    >>> fc = FullContact('your_api_key')
  
    # returns a real requests object
    >>> r = fc.api_get('person', **{'email': 'you@email.com'})
    >>> r.status_code
    200
    >>> r.headers['x-rate-limit-remaining']
    '59'
    >>> r.json()
    {u'socialProfiles': [...], u'demographics': {...}, ... }
    
    # for batched calls - a list of tuples like (endpoint, {params})
    >>> batch_calls = [
            ('disposable', {'email': 'this-is-a-fake-email@fake.com'}),
            ('person', {'email': 'email@gmail.com'}),
            ...
        ]
    >>> r2 = fc.api_batch(batch_calls)
    >>>

# FullContact API Documentation

Check out FullContact's documentation [here](http://www.fullcontact.com/developer/docs/).

# Tests

A limited test suite is available. Run with `nosetests` after installing, or if you're installing directly via `setup.py` you can use Nose's setuptools extension like so: `python setup.py install nosetests`
