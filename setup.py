#!/usr/bin/env python

from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
profile=pygments_profiles_syntax:ProfilesLexer
'''

setup(
    name='inventory-profiles-next-pygments_profiles_syntax',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.0.1'
    ]
)
