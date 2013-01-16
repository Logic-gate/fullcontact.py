# FullContact.py

A simple Python interface for [FullContact](http://www.fullcontact.com/), using Requests.

# Install

    pip install git+https://github.com/garbados/fullcontact.py.git

# Usage

    from fullcontact import FullContact

    fc = FullContact('your_api_key')
    person_profile = fc.get(email='you@email.com')

# FullContact API Documentation

Check out FullContact's documentation [here](http://www.fullcontact.com/developer/docs/).