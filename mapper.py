#!/usr/bin/env python

import sys

##      This code is written by S M Azharul Karim, Banner ID-01519097   ##
##      This is the mapper      ##
count=0
count1=0
for line in sys.stdin:
        line=line.strip()
        stadium, capacity, expanded, location, surface, turf, team, opened, weather, roof, elevation = line.split(",")
        # writing the output to STDOUT
        #output here will be input of reducer
        print '%s\t%s' %(turf,1)
