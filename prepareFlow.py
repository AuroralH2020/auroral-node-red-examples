#!/usr/bin/env python3

# This script is for removing OIDs and IDs from Auroral Nodes stored in flow
# usage ./prepareFlow inputfile.json outputfile.json
import json, sys

# arg test
if len(sys.argv) < 2:
    print('Please provide input file')
    exit(1)

# filenames
inputFileName = sys.argv[1]
outputFileName = 'output.json'
if len(sys.argv) > 2:
    outputFileName = sys.argv[2]

# Files
inputFile = None
outputFile = None
try:
    inputFile = open(inputFileName, "r")
except:
    print('Please check input file')
    exit(1)
try:
    outputFile = open(outputFileName, "w")
except:
    print('Please check output file')
    exit(1)
# Load JSON
try:
    inputJson = json.load(inputFile)
    outputJson = []
    # Process data
    for obj in inputJson:
        if obj['type'] == 'auroralDevice':
            obj['oid']= ''
            obj['td'] = obj['td']
            td = json.loads(obj['td'])
            # remove OID and IDs
            if 'oid' in td:
                del td['oid']
            if 'id' in td:
                del td['id']
            obj['td']= json.dumps(td, ensure_ascii=False, indent=4)
        outputJson.append(obj)
    # Store to output file
    json.dump(outputJson, outputFile, ensure_ascii=False, indent=4)
    # Close file
    outputFile.close()
    inputFile.close()
except:
  print("An exception occurred")
