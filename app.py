# install Pillow, numpy
from PIL import Image
import numpy as np
import sys, re

# Usage python app.py <file> <adjustment>
# eg. python app.py test.png -15

if __name__ == '__main__':
	# First parameter is the file.
	im = np.array(Image.open(sys.argv[1]).convert('L'))
		
	adj = 0
	# Second paramter is the 'adjustment'. 
	# Some images are too dark, the ranges can be adjusted in this way.
	if len(sys.argv) == 3:
		adj = int(sys.argv[2])

	finalOut = ''
	
	for line in im:
		lineOut = ''
		for item in line:
			if item in range(0 + adj, 85 + adj):
				item = ' '
			elif item in range(86 + adj, 170 + adj):
				item = '/'
			else:
				item = '#'
			lineOut = lineOut + item  + ' '
		
		# Add this line to the final output
		finalOut = finalOut + lineOut + '\n'
	
	# Swop test.png with test.txt for saving the output.
	r = re.compile('\..*')
	f = open(re.sub(r, '.txt', sys.argv[1],), "w")
	# Write the final output to a .txt file. 
	f.write(finalOut)
	f.close()