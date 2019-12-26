import requests
import json

BASE_URL = "http://127.0.0.1:8008/"
ENDPOINT_URL = "api/"


def get_list():
	r = requests.get(BASE_URL+ENDPOINT_URL+'api_list')
	return r.json()

# print(get_list())
get_list()

# def create_data():
# 	new_data = {
# 		'user': 1,
# 		'content': 'Some new text',
# 		'title': 'new text'
# 	}

# 	json_data = json.dumps(new_data)
# 	r = requests.post(BASE_URL+ENDPOINT_URL+'api_list/',data=json_data)
# 	print(r)
# 	print(r.headers)
# 	print(r.status_code)
# 	if r.status_code == 200:
# 		return r.json()

# 	return r.text()

# print(create_data())
