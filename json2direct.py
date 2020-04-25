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
    print 'sys.exit(1)'
    sys.exit(1)

# get the party results dictionaries
party_keys = election_data.get_party_keys(x)

# construct list of records
record_list = election_data.get_record_list(records, party_keys)

# find maximum possible length of each field
field_lengths = []
for field in record_list[0]:
    field_lengths.append(0)

for record in record_list:
    i = 0
    for field in record:
        field_length = len(field)
        if field_length > field_lengths[i]:
            field_lengths[i] = field_length
        i += 1

format_strings = []
i = 0
for x in record_list[0]:
    y = unicode(str(x))
    if y.isnumeric():
	format_strings.append('%' + str(field_lengths[i]) + 's')
    else:
	try:
	    float(x)
	    format_strings.append('%' + str(field_lengths[i]) + 's')
	except:
	    format_strings.append('%-' + str(field_lengths[i]) + 's')
    i += 1

# output block
filename = 'direct/' + os.path.splitext(os.path.basename(sys.argv[1]))[0] + '.dat'
outfile = open(filename, 'wb')

# output record rows
for record in record_list:
    i = 0
    for field in record:
	outfile.write(format_strings[i] % field)
	i += 1
outfile.close()
print 'processing complete - output dumped to file ' + filename
