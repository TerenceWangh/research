# Copyright 2020 The SevenDim Research.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Setup script for Research.
"""

from os import path
from setuptools import find_packages
from setuptools import setup

here = path.abspath(path.dirname(__file__))
install_requires = ['absl-py >= 0.2.2']
tests_require = ['nose']

description = (
    'SevenDim Research: A Research modules for deep learning in computer '
    'vision based on Tensorflow and TF-Slim.')

setup(
    name='7d-research',
    version='1.0.1',
    include_package_data=True,
    packages=find_packages(exclude=['docs']),
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='nose.collector',
    description=description,
    long_description=description,
    classifiers=[
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',

        # Pick your license as you wish
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

    ],
    license='Apache 2.0',
    keywords='tensorflow tf-slim python machine learning compute vision'
)
