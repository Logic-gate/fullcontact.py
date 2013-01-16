# FullContact.py

A simple Python interface for FullContact, using Requests.

# Install

    pip install git+https://github.com/garbados/fullcontact.py.git

# Usage

    from fullcontact import FullContact

    fc = FullContact('your_api_key')
    person_profile = fc.get(email='you@email.com')
