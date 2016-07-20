FullContact.py
==============

A Python interface for the [FullContact API](http://docs.fullcontact.com/).

Installation
------------

```
pip install fullcontact.py
```

Usage
-----


```python
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
```

Tests
-----

A limited test suite is available. Run with `nosetests` after installing, or if
you're installing directly via `setup.py` you can use Nose's setuptools
extension like so:

```
python setup.py install nosetests
```
