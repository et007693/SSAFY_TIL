import pprint
import requests

def get_deposit_products():
    params = {
    'auth' : api_key,
    'topFinGrpNo' : '020000',
    'pageNo' : 1
    }
    result = requests.get(url, params=params).json()
    diposit_list = []
    
    for fin in result['result']['baseList']:
        bank_dict = {'금리정보' : [], '금융상품명': '', '금융회사명' : ''}
        bank_dict['금융상품명'] = fin['fin_prdt_nm']
        bank_dict['금융회사명'] = fin['kor_co_nm']

        for info in result['result']['optionList']:
            if fin['fin_prdt_cd'] == info['fin_prdt_cd']:
                rate_dict = {
                    '저축 금리' : info['intr_rate'], 
                    '저축 기간' : info['save_trm'],
                    '저축금리유형' : info['intr_rate_type'],
                    '저축금리유형명' : info['intr_rate_type_nm'],
                    '최고 우대금리' : info['intr_rate2'],
                    }
                bank_dict['금리정보'].append(rate_dict)

        diposit_list.append(bank_dict)

    return diposit_list

if __name__ == '__main__':
    result = get_deposit_products()
    pprint.pprint(result)