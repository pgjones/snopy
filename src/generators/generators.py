#!/usr/bin/env python
#
# generators.py
#
# Holds a dictionary of all the generators
#
# Author P G Jones - 24/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import os
import inspect

generators = {}

def load_in_path(path):
    """ Load all the classes in a path."""
    global generators
    for module in os.listdir(path):
        if module[-3:] != '.py':
            continue
        package_set = __import__(module[:-3], locals(), globals())
        for name, obj in inspect.getmembers(package_set):
            if inspect.isclass(obj):
                instance_ = obj()
                generators[instance_.get_name()] = instance_

# First load in all the generators in the backgrounds folder
load_in_path(os.path.join(os.path.dirname(__file__), "backgrounds"))
load_in_path(os.path.join(os.path.dirname(__file__), "signals"))
