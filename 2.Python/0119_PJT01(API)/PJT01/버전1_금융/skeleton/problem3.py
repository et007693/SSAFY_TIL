import pprint
import requests


def get_deposit_products():
  params = {
    'auth' : api_key,
    'topFinGrpNo' : '020000',
    'pageNo' : 1
  }
  result = requests.get(url, params=params).json()
  doposit_list = []

  for fin in result['result']['optionList']:
    doposit_list.append({
       '금융상품코드' : fin['fin_prdt_cd'],
       '저축 금리' : fin['intr_rate'],
       '저축 기간' : fin['save_trm'],
       '저축금리유형' : fin['intr_rate_type'],
       '저축금리유형명' : fin['intr_rate_type_nm'],
       '최고 우대금리' : fin['intr_rate2']
    }) 

  return doposit_list

    
if __name__ == '__main__':
    result = get_deposit_products()
    pprint.pprint(result)