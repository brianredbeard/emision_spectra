#!/sw/bin/python
# -*- coding: utf-8 -*-

def angstromToRGB( wavelength, intensity ):
	return tuple( [x * intensity for x in [0.8, 0.8, 0.8]] );
