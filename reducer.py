#!/usr/bin/env python

from operator import itemgetter
import sys

##      this code is written by S M Azharul Karim, Banner ID-01519097   ##
##      This is the reducer     ##
current_countart = 0
current_countnatural = 0
current_turf=None
turf=None
## input comes from STDIN
for line in sys.stdin:
        ## remove leading and trailing whitespace
        line = line.strip()

        ## parse the input we got from mapper.py
        turf, count= line.split("\t",1)

         ## convert count (currently a string) to int
        try:
                count = int(count)
        except ValueError:
        ## count was not a number, so silently
        ## ignore/discard this line
                continue

        if current_turf==turf:
                current_countart=current_countart+1

    ## this IF-switch only works because Hadoop sorts map output
    ## by key (here: word) before it is passed to the reducer
        else:
                if current_turf:
                        current_countnatural += current_countnatural
                        #write result to STDOUT
                        print '%s\t%s' % (current_turf, current_countart)
                current_countart = count
                current_turf = turf


##      printing output to output directory
if current_turf == turf:
        print '%s\t%s' % (current_turf, current_countart)
        print "total no of artificial turfs:",current_countart
