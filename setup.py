#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import to get rid of an error in atexit._run_exitfuncs
import logging
import multiprocessing


try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name='tastypie-rpc-proxy',
    version='0.1.0',
    description='An extension of tastypie-queryset-client, designed intended for building RPC based on tastypie.',
    long_description=open('README.rst', 'r').read(),
    url='http://github.com/nk113/tastypie-rpc-proxy/',
    packages=find_packages(),
    package_data={'': ['*/fixtures/*.json']},
    zip_safe=False, 
    tests_require=('mock', 'django_nose',),
    test_suite = 'apps.test.runtests.runtests',
    install_requires=[
        'Django',
        'django-tastypie',
        'tastypie-queryset-client',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    author='Nobu Kakegawa',
    author_email='nobu@nk113.com',
)