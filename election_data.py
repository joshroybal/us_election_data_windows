# procedure definitions

# get the party headers from dictionaries - party: {"#":int,"%":flat,"ec":int}
def get_party_keys(x):
    party_keys = []
    for y in x:
        if y == 'margin': continue
        if isinstance(x[y], dict):
            for z in x[y]:
                party_keys.append([str(y), str(z)])
    return party_keys

# construct and return the list of headers
def get_header_list(party_keys):
    header_list = []
    header_list.append('state')
    header_list.append('electors')
    # append party results headers
    for key_list in party_keys:
        header_list.append(str(key_list[0]) + ' ' + str(key_list[1]))
    header_list.append('margin #')
    header_list.append('margin %')
    header_list.append('state total')
    return header_list

# construct and return list of records as list of field lists
def get_record_list(records, party_keys):
    us_total_record = []    # for tagging special U. S. Total record
    record_list = []
    # construct the list of fields
    for record in sorted(records):
        field_list = []
        field_list.append(str(record))
        field_list.append(str(records[record]['electors']))
        # get party data
        for key_list in party_keys:
            field_list.append(str(records[record][key_list[0]][key_list[1]]))
        field_list.append(str(records[record]['margin']['#']))
        field_list.append(str(records[record]['margin']['%']))
        field_list.append(str(records[record]['state total']))
        # append or tag the list of fields
        if field_list[0] == 'U. S. Total':
            # tag special U. S. Total record
            us_total_record = field_list
        else:
            record_list.append(field_list)
    # append special U. S. Total record
    record_list.append(us_total_record)
    return record_list
