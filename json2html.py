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
    print 'U. S. Total key not found - processing terminated'
    sys.exit(1)

# get the party results dictionaries
party_keys = election_data.get_party_keys(x)

# construct header list
header_list = election_data.get_header_list(party_keys)

# construct list of records
record_list = election_data.get_record_list(records, party_keys)

# output block
filename = 'html\\' + os.path.splitext(os.path.basename(sys.argv[1]))[0] + '.html'
outfile = open(filename, 'wb')
# output top of page html
outfile.write('<!DOCTYPE html>\r\n')
outfile.write('<html>\r\n')
outfile.write('<head>\r\n')
outfile.write('<link id="styleinfo" media="all">\r\n')
outfile.write('<script type="text/javascript" src="style.js" defer></script>\r\n')
outfile.write('</head>\r\n')
outfile.write('<body>\r\n')

# output html table
outfile.write('<table id="my_table">\r\n')

# output header row
outfile.write('<tr>')
for header in header_list:
    outfile.write('<th>' + header + '</th>')
outfile.write('</tr>\r\n')

# output record rows
for record in record_list:
    outfile.write('<tr>')
    for field in record:
	outfile.write('<td>' + field + '</td>')
    outfile.write('</tr>\r\n')
outfile.write('</table>\r\n')

# output bottom of page html
outfile.write('</body>\r\n')
outfile.write('</html>\r\n')
outfile.close()
print 'processing complete - output dumped to file ' + filename
