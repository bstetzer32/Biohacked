from urllib.request import Request, urlopen
from urllib.parse import urlencode
from json import loads
import os


def exrx_query(key, value):
    global_get_params = {key: value}
    username = os.environ['EXRX_USERNAME']  # declare username in .env file
    password = os.environ['EXRX_PASSWORD']  # declare password in .env file
    credentials = {"username": username, "password": password}
    galh = "204.235.60.194"  # global_auth_link_host
    galp = "/consumer/login"  # global_auth_link_path
    grh = "204.235.60.194"  # global_request_host
    grp = "/exrxapi/v1/allinclusive/exercises"  # global_request_path
    req_string = f'http://{grh}{grp}?{urlencode(global_get_params)}'
    res = urlopen(Request(f'http://{galh}{galp}',
                  data=urlencode(credentials).encode()))
    token = loads(res.read().decode('utf-8'))['token']
    res = urlopen(Request(req_string,
                  headers={"Authorization": f'Bearer {token}'}))
    return loads(res.read().decode('utf-8'))
