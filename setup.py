"""
FullContact.py
--------------

Simple Python interface for FullContact, using Requests.

"""
from setuptools import setup


setup(
    name='FullContact.py',
    version='0.0.3',
    url='https://github.com/garbados/fullcontact.py',
    license='MIT',
    author=['Max Thayer', 'Amer Almadani', 'Brendan Maione-Downing'],
    author_email=['garbados@gmail.com', 'mad_dev@linuxmail.org', 'b.maionedowning@gmail.com'],
    description='Simple Python interface for FullContact, using Requests',
    long_description=open('README.txt', 'r').read(),
    packages=['fullcontact'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    tests_require=[
        'nose>=1.0',
    ],
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
