#!/usr/bin/env python

from setuptools import setup, find_packages


test_requirements = ['mock', 'pytest', 'pytest-cov']
setup(
    name='nap',
    version="0.2.5",
    description=('api access modeling and tools'),
    author="Jacob Burch",
    author_email="jacobburch@gmail.com",
    url='https://github.com/jacobb/nap',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    requires=[
    ],
    zip_safe=False,
    tests_require=test_requirements,
    install_requires=[
        'slumber>=0.4.2',
    ] + test_requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
