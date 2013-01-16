"""
FullContact.py
--------------

Simple Python interface for FullContact, using Requests.

"""
from setuptools import setup


setup(
    name='FullContact.py',
    version='0.0.1',
    url='https://github.com/garbados/fullcontact.py',
    license='MIT',
    author='Max Thayer',
    author_email='garbados@gmail.com',
    description='Simple Python interface for FullContact, using Requests',
    long_description=file.read(open('README.md', 'r')),
    packages=['fullcontact'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    tests_require=[
        'Attest',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
