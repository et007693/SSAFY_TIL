import pprint
import requests


def get_deposit_products():
  params = {
    'auth' : api_key,
    'topFinGrpNo' : '020000',
    'pageNo' : 1
  }
  result = requests.get(url, params=params).json()
  
  return result['result']['baseList']

    
if __name__ == '__main__':
    result = get_deposit_products()
    pprint.pprint(result)