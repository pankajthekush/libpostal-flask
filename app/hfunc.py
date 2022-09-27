import os

"""
helper function to do database stuff which do not have to do anything with sqlalchmey.
"""


def get_pg_conn_str():

    return 'sqlite:///locdb.db'

    """
        returns postgres connection string , access values from env variables
        if not found ask user
    """  
    data_dict = {'DBNAME':None,'DUSER':None,'HOST':None,'PASSWORD':None,'APPNAME':None}

    for dkey in list(data_dict.keys()):
        d_val = os.environ[dkey]
        data_dict[dkey] = d_val


    # now get enviornment and create conn string
    connstring = 'postgresql+psycopg2://{}:{}@{}/{}?application_name={}'.format(data_dict['DUSER'], \
                data_dict['PASSWORD'],data_dict['HOST'],data_dict['DBNAME'],data_dict['APPNAME'])
    return connstring

PG_CONN_STR = get_pg_conn_str()