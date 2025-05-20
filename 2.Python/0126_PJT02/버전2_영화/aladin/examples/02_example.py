
import requests
from pprint import pprint
import json



query_type = 'ItemNewSpecial'
max_results = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101

URL = f'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={ttbkey}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}'

response = requests.get(URL)

response_json = response.json()

pprint(response_json)



URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'

params = {
    'QueryType': 'ItemNewAll',
    'MaxResults': 20,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101',
}

response = requests.get(URL, params=params).json()
pprint(response['item'])
