#!/sw/bin/python
# -*- coding: utf-8 -*-

def angstromToRGB( wavelength, intensity ):
	if( wavelength < 3800 ):
		wavelengthColour = (0.0, 0.0, 0.0);
	# violet
	if( wavelength >= 3800 and wavelength < 4200 ):
		wavelengthColour = (0.5, 0.0, 1.0);
	# indigo
	if( wavelength >= 4200 and wavelength < 4400 ):
		wavelengthColour = (0.3, 0.0, 0.5);
	# blue
	if( wavelength >= 4400 and wavelength < 5200 ):
		wavelengthColour = (0.0, 0.0, 1.0);
	# green
	if( wavelength >= 5200 and wavelength < 5700 ):
		wavelengthColour = (0.0, 1.0, 0.0);
	# yellow
	if( wavelength >= 5700 and wavelength < 5850 ):
		wavelengthColour = (1.0, 1.0, 0.0);
	# orange
	if( wavelength >= 5850 and wavelength < 6300 ):
		wavelengthColour = (1.0, 0.5, 0.0);
	# red
	if( wavelength >= 6300 and wavelength < 7400 ):
		wavelengthColour = (1.0, 0.0, 0.0);
	if( wavelength >= 7400 ):
		wavelengthColour = (0.0, 0.0, 0.0);
	return tuple( [x * intensity for x in wavelengthColour] );
