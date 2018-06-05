#!/usr/bin/env python

# Copyright 2018 Stavros Sachtouris
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from dis import __version__

setup(
    name='docker-image-size',
    version=__version__,
    description=('Get the size of a docker image without downloading it.'),
    long_description=open('README.md').read(),
    url='',
    download_url='',
    license='GPLv3',
    author='Stavros Sachtouris',
    author_email='saxtouri@gmail.com',
    maintainer='Stavros Sachtouris',
    maintainer_email='saxtouri@gmail.com',
    packages=['dis', ],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'docker-image-size = dis.cli:cli',
        ]
    },
    install_requires=[]
)
