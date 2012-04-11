#!/usr/bin/env python

from distutils.core import setup

from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
setup(name = 'sigintwrap',
        version = '0.0.1',
        description = 'Wrapper to forward TERM signals to INT signals so uWSGI plays nice with runit',
        author = 'Josh Bryan',
        author_email = 'jbryan@ci.uchicago.edu',
        url = 'https://globusonline.github.com/sigint',
        classifiers = [
              'Programming Language :: Python :: 2',
           ],
        scripts = ['./sigintwrap']
        )
