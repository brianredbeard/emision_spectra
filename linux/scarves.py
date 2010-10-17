#!/sw/bin/python
# -*- coding: utf-8 -*-

# This work is licensed under a Creative Commons Attribution-Share Alike 2.5 Australia License.

import math;
import spectra;

# default
from colourmodel_bruton import angstromToRGB;

blackWool = ( 0.0, 0.0, 0.0 );

def addNStitches( n, c ):
	return [ c ] * int( n );

# needs work
def visualIntensityToColumns( i, maxIntensity ):
	if( i / maxIntensity > 0.85 ):
		return 3;
	if( i / maxIntensity > 0.50 ):
		return 2;
	else:
		return 1;

def findSpectra( element ):
	return spectra.spectra[ element ];

def designScarf( totalLength, stitchLength, borderLength, element, lowerBand, upperBand ):
	pattern = [];
	lengthInStitches = math.ceil( float( totalLength ) / stitchLength );
	borderLengthInStitches = math.floor( float( borderLength ) / stitchLength );
	pattern.extend( addNStitches( borderLengthInStitches, blackWool ) );
	
	# create our canvas:
	workspaceStitches = addNStitches( math.ceil( lengthInStitches - 2 * borderLengthInStitches ), blackWool );
	
	# work through our element:
	spectralLines = [ x for x in findSpectra( element ) if x[1] >= lowerBand and x[1] <= upperBand ];

	totalIntensities = {};
	wavelengths = {};
	for line in spectralLines:
		intensity, wavelength = line;
		wavelengthPosition = ( wavelength - lowerBand ) / ( upperBand - lowerBand );
		stitchingRow = int( math.floor( wavelengthPosition * len( workspaceStitches ) ) );
		totalIntensities[ stitchingRow ] = totalIntensities.get( stitchingRow, 0 ) + intensity;
		if not wavelengths.has_key( stitchingRow ):
			wavelengths[ stitchingRow ] = [ wavelength ];
		else:
			wavelengths[ stitchingRow ].append( wavelength );

	# Very bright emissions bleed to the right, all emissions are presented at
	# full intensity. This will save us having to track down one million different 
	# shades of wool.
	maxIntensity = max( totalIntensities.values() + [0] );
	for stitchingRow in totalIntensities.keys():
		paintIntensity = visualIntensityToColumns( totalIntensities[ stitchingRow ], maxIntensity );
		paintPosition = stitchingRow;
		paintColour = angstromToRGB( sum( wavelengths[ stitchingRow ] ) / len( wavelengths[ stitchingRow ] ), 1 );
		while( paintIntensity > 0 ):
			workspaceStitches[ min( paintPosition, len( workspaceStitches ) - 1 ) ] = paintColour;
			paintIntensity -= 1;
			paintPosition += 1;
	
	pattern.extend( workspaceStitches );
	pattern.extend( addNStitches( borderLengthInStitches, blackWool ) );
	return pattern;

def makeColourBlock( col, width = 16, suppressHex = False ):
	retValue = "<span style='background-color:#%02x%02x%02x'>%s</span>" % ( col[0] * 255, col[1] * 255, col[2] * 255, "&nbsp;" * width );
	#retValue = "<span style='color:#%02x%02x%02x'>%s</span>" % ( col[0] * 255, col[1] * 255, col[2] * 255, "█" * width );
	if( not suppressHex ):
		retValue += "<tt>( #%02x%02x%02x )</tt>" % ( col[0] * 255, col[1] * 255, col[2] * 255 );
	return retValue;

def prettyPrintPatternHTML( pattern ):
	retValue = "<table cols=2 width=\"100%\">";
	currentColour = None;
	currentCount = 0;
	colourUsage = {};
	for p in pattern:
		colourUsage[ p ] = colourUsage.get( p, 0 ) + 1;
		if( p != currentColour ):
			if( currentColour != None ):
				retValue += "<tr><td>&nbsp;&nbsp;%i row" % currentCount;
				if( currentCount > 1 ):
					retValue += "s";
				retValue += " of</td><td>%s</td></tr>" % makeColourBlock( currentColour );
			currentColour = p;
			currentCount = 1;
		else:
			currentCount += 1;
	retValue += "<tr><td>&nbsp;&nbsp;%i row" % currentCount;
	if( currentCount > 1 ):
		retValue += "s";
	retValue += " of</td><td>%s</td></tr></table>" % makeColourBlock( currentColour );
	retValue += "<p><em>Preview:</em><blockquote>";
	for p in pattern:
		retValue += makeColourBlock( p, 1, True );
	retValue += "</blockquote></p>";
	retValue += "<p><em>Shopping list:</em><blockquote>";
	for col in sorted( colourUsage.keys() ):
		retValue += "%s&nbsp;x&nbsp;%i row" % ( makeColourBlock( col ), colourUsage[ col ] );
		if( colourUsage[ col ] > 1 ):
			retValue += "s";
		retValue += ", ";
	retValue = retValue[ : -2 ];
	retValue += "</blockquote></p>";
	return retValue;
