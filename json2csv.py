#!/usr/bin/env python

import json
import sys
import os
import election_data

# input block
if len(sys.argv) < 2:
    print 'Usage: ' + sys.argv[0] + ' filename'
    sys.exit(1)

filename = sys.argv[1]
try:
    infile = open(filename, 'rb')
except:
    print 'error opening file ' + filename
    sys.exit(1)
records = json.load(infile)
infile.close()

# processing block
try:
    x = records['U. S. Total']
except:
    print 'record not found'
    sys.exit(1)

# get the party results dictionaries
party_keys = election_data.get_party_keys(x)

# get the list of headers
header_list = election_data.get_header_list(party_keys)

# get the list of records
record_list = election_data.get_record_list(records, party_keys)

# output block
filename = 'csv/' + os.path.splitext(os.path.basename(sys.argv[1]))[0] + '.csv'
outfile = open(filename, 'wb')

# output header row
outfile.write(header_list[0])
for header in header_list[1:]:
    outfile.write(',' + header)
outfile.write('\r\n')

# output state record rows
for record in record_list:
    outfile.write(record[0])
    for field in record[1:]:
        outfile.write(',' + field)
    outfile.write('\r\r\n')
outfile.close()
print 'processing complete - output dumped to file ' + filename
