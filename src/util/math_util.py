#!/usr/bin/env python
#
# math_util.py
#
# The useful math functions
#
# Author P G Jones - 21/02/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import math

def poisson(l, k):
    """ Return Poisson value P(k=k | l), l is lambda but lambda is special in python."""
    k = int(k)
    l = float(l)
    return math.pow(l, k) * math.exp( -l ) / math.factorial(k)
