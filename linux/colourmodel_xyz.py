#!/sw/bin/python
# -*- coding: utf-8 -*-
import math;

# thank you to Nino Cutic for providing me with this lookup table and correction factor set

fh = open( "lambdargb.dat" );
lines = fh.readlines();
fh.close();

wavelengths = {};
maxValue = 0;
for l in lines:
	w, x, y, z = [ float( x ) for x in l.split() ];
	r = 2.36461 * x -0.89654 * y -0.46807 * z;
	g = -0.81517 * x + 1.42641 * y + 0.08876 * z;
	b = 0.00520 * x -0.01441 * y + 1.00920 * z;
	maxValue = max( maxValue, max( [ r, g, b ] ) );
	wavelengths[ w ] = ( r, g, b );

for w in wavelengths:
	wavelengths[ w ] = [ max( x / maxValue, 0 ) for x in wavelengths[ w ] ];
	
def angstromToRGB( wavelength, intensity, rainbow = False ):
	wavelengthColour = wavelengths.get( math.floor( wavelength / 10.0 ), (0.0, 0.0, 0.0) );
	return tuple( [x * intensity for x in wavelengthColour] );

