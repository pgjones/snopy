#!/usr/bin/env python
import math
# Author P G Jones - 22/06/2011 <p.g.jones@qmul.ac.uk>
# Helpful Math Functions 

def PoissonValue( l, k ):
    """ Return Poisson value P(k=k | l), l is lambda but lambda is special in python."""
    k = int(k)
    l = float(l)
    return math.pow( l, k ) * math.exp( -l ) / Factorial( k ) # math.Factorial( k ) only 2.6 onwards :( 

def Factorial( k ):
    """ Return k!."""
    if k == 0:
        return 1
    val = k
    for i in range( k - 1, 0, -1 ):
        val = val * i
    return val
