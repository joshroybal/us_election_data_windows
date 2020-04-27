#!/usr/bin/env python

import json
import sys
import os
import election_data

# construct and return list of maximum possible field lengths
def get_field_lengths(header_list, record_list):
    field_lengths = []
    for header in header_list:
        field_lengths.append(len(header))
    for record in record_list:
        i = 0
        for field in record:
            field_length = len(field)
            if field_length > field_lengths[i]:
                field_lengths[i] = field_length
            i += 1
    return field_lengths

# construct and return list of format strings for flat file output
def get_format_strings(record_list):
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
    return format_strings

# input block
if len(sys.argv) < 2:
    print 'Usage: ' + sys.argv[0] + ' filename csv|tab|flat|html'
    sys.exit(1)

flag = sys.argv[2]
if flag != 'csv' and flag != 'tab' and flag != 'flat' and flag != 'html':
    print 'Usage: ' + sys.argv[0] + ' filename csv|tab|flat|html'
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

if flag == 'flat':
    field_lengths = get_field_lengths(header_list, record_list)
    format_strings = get_format_strings(record_list)

# output block
filename = flag + '\\' + os.path.splitext(os.path.basename(sys.argv[1]))[0] + '.' + flag
outfile = open(filename, 'wb')

# output top of page html
if flag == 'html':
    outfile.write('<!DOCTYPE html>\n')
    outfile.write('<html>\n')
    outfile.write('<head>\n')
    outfile.write('<link id="styleinfo" media="all">\n')
    outfile.write('<script type="text/javascript" src="style.js" defer></script>\n')
    outfile.write('</head>\n')
    outfile.write('<body>\n')
    outfile.write('<table id="my_table">\n')
    outfile.write('<tr>')

# output header row
for header in header_list[:-1]:
    i = 0
    if flag == 'html': outfile.write('<th>')
    if flag == 'flat':
        outfile.write(format_strings[i] % header)
    else:
        outfile.write(header)
    if flag == 'csv': outfile.write(',')
    if flag == 'tab': outfile.write('\t')
    if flag == 'html': outfile.write('</th>')
    i += 1
if flag == 'html': outfile.write('<th>')
if flag == 'flat':
    outfile.write(format_strings[-1] % header_list[-1])
else:
    outfile.write(header_list[-1])
if flag == 'html': outfile.write('</th></tr>')
outfile.write('\n')

# output state record rows
for record in record_list:
    if flag == 'html': outfile.write('<tr>')
    for field in record[:-1]:
        i = 0
        if flag == 'html': outfile.write('<td>')
        if flag == 'flat':
            outfile.write(format_strings[i] % field)
        else:
            outfile.write(field)
        if flag == 'csv': outfile.write(',')
        if flag == 'tab': outfile.write('\t')
        if flag == 'html': outfile.write('</td>')
        i += 1
    if flag == 'html': outfile.write('<td>')
    if flag == 'flat':
        outfile.write(format_strings[-1] % record[-1])
    else:
        outfile.write(record[-1])
    if flag == 'html': outfile.write('</td></tr>')
    outfile.write('\n')

# output bottom of page html
if flag == 'html':
    outfile.write('</table>\n')
    outfile.write('</body>\n')
    outfile.write('</html>\n')

outfile.close()
print 'processing complete - output dumped to file ' + filename
