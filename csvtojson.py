import csv
import sys
import json

inputFile  = sys.argv[1]
outputFile = inputFile +".json"


with open( inputFile, 'r') as csvFile:
csvReader = csv.DictReader( csvFile)
allRows   = list( csvReader )
json.dump( allRows,open( outputFile, 'w' ) )