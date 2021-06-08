from urllib.request import Request, urlopen
from urllib.parse import urlencode, unquote
from json import loads, dumps

# ids = str.join()
global_get_params = {"exerciseids": "[]"}
# "exercisename": "Standing", "apparatus":"[lever,cable,barbell,dumbbell]",
#  "bodypart":"Shoulders"
# credentials = {"username":"YOUR_USERNAME","password":"YOUR_PASSWORD"}
credentials = {"username": "benjaminsexrx", "password": "kL5gus3h"}
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
print(loads(res.read().decode('utf-8')))
