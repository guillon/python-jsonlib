#!/usr/bin/env python
#
# Copyright (C) STMicroelectronics Ltd. 2012
#
# Licensed under the MIT licence: 
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

from distutils.core import setup
import jsonlib as module

name = module.__name__
version = module.__version__
url_base = "http://tobedefined/"
url = url_base + '#' + name
download_url = "%sdownload/%s-%s.tar.gz" % (url_base, name, version)
# extract description and long_description from module __doc__ string
lines = module.__doc__.split("\n")
while len(lines) > 0 and lines[0] == '':
    lines.pop(0)
empty = lines.index('')
descr = '\n'.join(lines[:empty])
long_descr = '\n'.join(lines[empty+1:])

setup(name=name,
      version=version,
      description=descr,
      long_description=long_descr,
      author="Christophe Guillon",
      author_email="christophe.guillon.perso@gmail.com",
      url=url,
      download_url=download_url,
      py_modules=['jsonlib/__init__', 'jsonlib/base', 'jsonlib/search'],
      classifiers=[
        'Development Status :: 3 - Alpha',
        #"Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        # Want: 'Topic :: Text Processing :: Markup :: JSON'
        'Topic :: Text Processing :: Markup'
        ],
      license="MIT",
      platforms = ['Any']
      )
