#!/usr/bin/env python

import sys
import json
import os

#initialization block
candidates = {}
parties = []
records = {}

#input block
filename = sys.argv[1]
infile = open(filename, 'rb')
for line in infile:
    fields = line.strip().split('\t')
    if len(fields) > 2:
        state = fields[0]
        record = {}
        i = 2
        for party in parties:
            tmp = {}
            try:
                tmp['#'] = int(fields[i].replace(',', ''))
            except:
                tmp['#'] = 0
            try:
                tmp['%'] = float(fields[i+1].replace('%', ''))
            except:
                tmp['%'] = 0.
            try:
                tmp['ec'] = int(fields[i+2].replace(',', ''))
            except:
                tmp['ec'] = 0
            i += 3
            record[party] = tmp
        tmp = {}
        try:
            tmp['#'] = int(fields[i].replace(',', ''))
            tmp['%'] = float(fields[i+1].replace('%', ''))
        except:
            tmp['#'] = 0
            tmp['%'] = 0.
        record['margin'] = tmp
        # record['state total'] = int(fields[i+2].replace(',', ''))
        try: record['state total'] = int(fields[i+2].replace(',', ''))
        except: record['state total'] = 0
        record['electors'] = fields[1]
        records[state] = record
    elif len(fields) == 2:
        candidates[fields[1]] = fields[0]
        parties.append(fields[1])
infile.close()

# output block
filename = 'json\\' + os.path.splitext(os.path.basename(sys.argv[1]))[0] + '.json'
jsonfile = open(filename, 'wb')
#json.dump(records, jsonfile)
# Compact enoding:
# json.dump(records, jsonfile, separators=(',',':'))
# Pretty printing:
json.dump(records, jsonfile, indent=4, separators=(',', ': '))
jsonfile.close()
print 'data dumped to file ' + filename
