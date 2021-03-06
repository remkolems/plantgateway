#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################
#
# This is open source software licensed under the Apache License 2.0
# http://www.apache.org/licenses/LICENSE-2.0
#
##############################################
"""Setup for plantgateway."""
from setuptools import setup
from plantgw import __version__


def readme():
    """Load the readme file."""
    with open('README.md', 'r') as readme_file:
        return readme_file.read()


setup(
    name='plantgateway',
    version=__version__,
    description='Bluetooth to mqtt gateway for Xiaomi Mi plant sensors',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Christian Kühnel',
    author_email='christian.kuehnel@gmail.com',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=['plantgw'],
    install_requires=['bluepy==1.3.0', 'paho-mqtt', 'pyyaml>=5.1', 'miflora==0.6', 'typing>=3,<4'],
    scripts=['plantgateway'],
    )
