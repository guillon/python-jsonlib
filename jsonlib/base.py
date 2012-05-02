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

"""
A simple modification library for hierachical dictionaries.
"""

def add_item(obj, path, value):
    """ Add a new item value. Return value or False if already defined. """
    items = path.split(".")
    for i in items[:len(items)-1]:
        if not i in obj:
            obj[i] = {}
        obj = obj[i]
    if items[len(items)-1] in obj:
        return False
    obj[items[len(items)-1]] = value
    return value

def update_item(obj, path, value):
    """ Update an existing item. Return new value or False if not defined. """
    items = path.split(".")
    for i in items[:len(items)-1]:
        if not i in obj:
            return False
        obj = obj[i]
    if not items[len(items)-1] in obj:
        return False
    obj[items[len(items)-1]] = value
    return value

def get_item(obj, path):
    """ Get an existing item value. Return value or False if not defined. """
    items = path.split(".")
    for i in items[:len(items)-1]:
        if not i in obj:
            return False
        obj = obj[i] 
    if not items[len(items)-1] in obj:
        return False
    return obj[items[len(items)-1]]

def weak_item(obj, path, value):
    """ Weakly set item value or ignore if already defined. Return actual item value. """
    items = path.split(".")
    for i in items[:len(items)-1]:
        if not i in obj:
            obj[i] = {}
        obj = obj[i]
    if not items[len(items)-1] in obj:
        obj[items[len(items)-1]] = value
    return obj[items[len(items)-1]]

def set_item(obj, path, value):
    """ Set item value. Return value. """
    items = path.split(".")
    for i in items[:len(items)-1]:
        if not i in obj:
            obj[i] = {}
        obj = obj[i]
    obj[items[len(items)-1]] = value
    return value

def remove_item(obj, path):
    """ Remove item. Return previous value or False if not defined. """
    items = path.split(".")
    for i in items[:len(items)-1]:
        if not i in obj:
            return False
        obj = obj[i]
    if not items[len(items)-1] in obj:
        return False
    return obj.pop(items[len(items)-1])
