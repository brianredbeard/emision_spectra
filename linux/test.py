#!/usr/bin/python

#import colourmodel_rainbow
from colourmodel_monotone import angstromToRGB
colourModule = __import__( "colourmodel_rainbow" );

#def angstromToRGB( wavelength, intensity ):
import scarves;
scarves.angstromToRGB = colourModule.angstromToRGB;
#if( singleStripes ):
        #scarves.visualIntensityToColumns = lambda x, y: 1;
#        pass;
totalLength = 200
borderLength = 2.5
rowLength = 0.5
lowerBand = 4000
upperBand = 7500
fh = open( "formtop.html", "r" );
x = fh.read();
fh.close();
element = "Si"
x += scarves.prettyPrintPatternHTML( scarves.designScarf( totalLength, rowLength, borderLength, element, lowerBand, upperBand ) );

fh = open( "formbottom.html", "r" );
x += fh.read();
fh.close();
print x;

