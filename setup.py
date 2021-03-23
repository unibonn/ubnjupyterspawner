#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

#-----------------------------------------------------------------------------
# Minimal Python version sanity check (from IPython/Jupyterhub)
#-----------------------------------------------------------------------------

from __future__ import print_function

import os
import sys

from distutils.core import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))

# Get the current package version.
version_ns = {}
with open(pjoin(here, 'version.py')) as f:
    exec(f.read(), {}, version_ns)

setup_args = dict(
    name                = 'ubnjupyterspawner',
    packages            = ['ubnspawner'],
    include_package_data = True,
    version             = version_ns['__version__'],
    description         = """UBNspawner: A spawner modification of WrapSpawner for JupyterHub based on SDCC/ND version.""",
    long_description    = "",
    author              = "Oliver Freyermuth",
    author_email        = "freyermuth@physik.uni-bonn.de",
    url                 = "https://github.com/unibonn/",
    license             = "BSD",
    platforms           = "Linux, Mac OS X",
    keywords            = ['Interactive', 'Interpreter', 'Shell', 'Web'],
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)

# setuptools requirements
install_requires = ["wrapspawner"]
dependency_links = [
    "git+https://github.com/jupyterhub/wrapspawner#egg=wrapspawner"
]

if 'setuptools' in sys.modules:
    setup_args['install_requires'] = install_requires
    setup_args['dependency_links'] = dependency_links

def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()
