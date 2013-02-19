#!/usr/bin/env python
#
# limit_techniques.py
#
# Classes to calculate the limits under differing statistical techniques. Returns a limit.
#
# Author P G Jones - 28/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import limit_set

class LimitCalculator(object):
    def __init__(self, detected_data_set, technique, data=None):
        """ Initialise the limit calculator."""
        self._data_set = detected_data_set
        self._technique = technique
        self._data = data
    def calculate(self):
        """ Calculate the limits for the years suggested."""
        result_set = limit_set.SignalLimitSet()
        for year in [1.0, 2.0, 3.0, 4.0]:
            self._data_set.scale_years(year)
            data = self._data
            if data is None:
               data = self._data_set.get_summed_background()
            result_set.add(year, self._technique.calculate(self._data_set, data))
        return result_set
