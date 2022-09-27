from flask import Blueprint, request
import logging,sys, json
from ipostal import ipost_parse

#loging
formatter = logging.Formatter(fmt='%(asctime)s %(name)s %(process)d %(levelname)-8s %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
#end logging

api_postal = Blueprint('api_postal',__name__)

@api_postal.route('/parser',methods=['POST'])
def iparse():
    json_data = request.get_json()
    str_add = json_data['query']
    dict_data = ipost_parse(str_address=str_add)
    return json.dumps(dict_data)