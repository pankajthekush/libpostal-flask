from postal.expand import expand_address 
from postal.parser import parse_address


def ipost_parse(str_address):
    parsed_ad = parse_address(str_address)
    dict_data = {tup[1]:tup[0] for tup in parsed_ad}    
    return dict_data