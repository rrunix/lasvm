#! /usr/bin/env python
#
# Copyright (C) 2012 Mathieu Blondel

import sys
import os
from Cython.Build import cythonize

DISTNAME = 'lasvm'
DESCRIPTION = "Efficient Lasvm python implementation"
LONG_DESCRIPTION = open('README.md').read()
MAINTAINER = 'Ruben Rodriguez'
MAINTAINER_EMAIL = 'ruben.rrf93@gmail.com'
URL = 'https://github.com/rrunix/lasvm'
LICENSE = 'new BSD'
DOWNLOAD_URL = 'https://github.com/rrunix/lasvm'
VERSION = '0.1-git'

INSTALL_REQUIRES = ['scikit-learn>=0.21.0', 'cython>=0.29', 'numpy>=1.17.0']

import setuptools  # we are using a setuptools namespace
from numpy.distutils.core import setup


def configuration(parent_package='', top_path=None):
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.add_subpackage('lasvm')
    config.ext_modules = cythonize(config.ext_modules, compiler_directives={'language_level' : "3"})
    return config

if __name__ == "__main__":

    old_path = os.getcwd()
    local_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    os.chdir(local_path)
    sys.path.insert(0, local_path)

    setup(configuration=configuration,
          name=DISTNAME,
          maintainer=MAINTAINER,
          include_package_data=True,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=LONG_DESCRIPTION,
          zip_safe=False, # the package can run out of an .egg file,
          install_requires=INSTALL_REQUIRES,
          classifiers=[
              'Intended Audience :: Science/Research',
              'Intended Audience :: Developers',
              'License :: OSI Approved',
              'Programming Language :: C',
              'Programming Language :: Python',
              'Topic :: Software Development',
              'Topic :: Scientific/Engineering',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'
             ]
    )

