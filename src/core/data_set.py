#!/usr/bin/env python
#
# data_set.py
#
# Data set containers
#
# Author P G Jones - 23/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import ROOT
import spectrum_util

class DataSet(object):
    """ Container for data sets."""
    def __init__(self, name):
        """ Initialise the data set."""
        self._backgrounds = []
        self._signal = None
        self._name = name
    def add_background(self, background):
        """ Add a background to the data set."""
        if not self._check_type(background):
            raise Exception("Wrong data set type.")
        self._backgrounds.append(background)
    def add_backgrounds(self, backgrounds):
        """ Add a list of backgrounds to the data set."""
        for background in backgrounds:
            self.add_background(background)
    def set_signal(self, signal):
        """ Set the data set signal."""
        if not self._check_type(signal):
            raise Exception("Wrong data set type.")
        self._signal = signal
    def iter_backgrounds(self):
        """ Iterate over the backgrounds."""
        for data_set in self._backgrounds:
            yield data_set
    def get_background(self, name):
        """ Return the backgorund with name."""
        for background in self.iter_backgrounds():
            if background.GetName() == name:
                return background
        return None
    def get_summed_background(self, name="Temp"):
        """ Return a summed background with name."""
        summed_background = self._new_data(name)
        for background in self.iter_backgrounds():
            summed_background.Add(background)
        return summed_background
    def get_signal(self):
        """ Return the signal."""
        return self._signal
    ################################################################################################
    def _check_type(self, data_set):
        """ Returns true if data_set is of the correct type."""
        pass
    def _new_data(self, name):
        """ Reutrn an empty data type."""
        pass

class RawDataSet(DataSet):
    """ Container for raw data sets."""
    def __init__(self, name):
        super(RawDataSet, self).__init__(name)
    def _check_type(self, data_set):
        """ Returns true if data_set is of the correct type."""
        return isinstance(data_set, ROOT.TH2D)
    def _new_data(self, name):
        """ Reutrn an empty data type."""
        return spectrum_util.default_raw(name)

class DetectedDataSet(DataSet):
    """ Container for detected data sets."""
    def __init__(self, name):
        super(DetectedDataSet, self).__init__(name)
        self._years = 1.0
    def _check_type(self, data_set):
        """ Returns true if data_set is of the correct type."""
        return isinstance(data_set, ROOT.TH1D)
    def _new_data(self, name):
        """ Reutrn an empty data type."""
        return spectrum_util.default_detected(name)
    def set_signal(self, signal, raw_count):
        """ Set the detected signal, taking account of the efficiency in detection."""
        super(DetectedDataSet, self).set_signal(signal)
        self._efficiency = signal.GetSumOfWeights() / raw_count
    def scale_years(self, num_years):
        """ Scale the data to num_years worth."""
        for background in self.iter_backgrounds():
            background.Scale(num_years/self._years)
        self._signal.Scale(num_years/self._years)
        self._years = num_years
