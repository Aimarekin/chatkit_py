#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pusher'
]

setup_requirements = [
    # TODO(iMerica): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='chatkit_server_python',
    version='0.1.0',
    description="A Python Port of https://github.com/pusher/chatkit-server-ruby",
    long_description=readme + '\n\n' + history,
    author="Michael Martinez",
    author_email='michaelmartinez@me.com',
    url='https://github.com/iMerica/chatkit_server_python',
    packages=find_packages(include=['chatkit_server_python']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='chatkit_server_python',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
