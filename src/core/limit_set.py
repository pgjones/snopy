#!/usr/bin/env python
#
# limit_set.py
#
# Limit set containers
#
# Author P G Jones - 29/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################

class SignalLimitSet(object):
    """ Container for limit sets."""
    def __init__(self):
        """ Initialise this limit set."""
        self._years = []
        self._limit = []
    def add(self, year, limits):
        """ Add a new limits."""
        self._years.append(year)
        self._limit.append(limits)
    def iter_limits(self):
        """ Yield a year, limit tuple for each limit."""
        for year_limit in zip(self._years, self._limit):
            yield year_limit
