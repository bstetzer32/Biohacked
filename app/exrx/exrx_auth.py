from urllib.request import Request, urlopen
from urllib.parse import urlencode, unquote
from json import loads, dumps

global_get_params = {"exercisename": "burpee"}
# credentials = {"username":"YOUR_USERNAME","password":"YOUR_PASSWORD"}
credentials = {"username":"benjaminsexrx","password":"kL5gus3h"}
global_auth_link_host = "204.235.60.194"
global_auth_link_path = "/consumer/login"
global_request_host = "204.235.60.194"
global_request_path = "/exrxapi/v1/allinclusive/exercises"
user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13"

res = urlopen(Request(f'http://{global_auth_link_host}{global_auth_link_path}', data=urlencode(credentials).encode()))
token = loads(res.read().decode('utf-8'))['token']
res = urlopen(Request(f'http://{global_request_host}{global_request_path}?{urlencode(global_get_params)}', headers={"Authorization": f'Bearer {token}'}))
print(loads(res.read().decode('utf-8')))