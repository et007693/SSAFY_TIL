import requests
from pprint import pprint

URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

params = {
    'ttbkey' : 'ttbthdckddyd1231146001',
    'QueryType' : 'Title',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101',
    'OptResult' : 'ebookList'
}

def ebook_list(title):
    # 여기에 코드를 작성합니다.
    ebook_list = []
    
    params['Query'] = title
    response = requests.get(URL, params=params).json()

    try:
        pa_price = response['item'][0]['priceSales']
        eb_price = response['item'][0]['subInfo']['ebookList'][0]['priceSales']
        if eb_price <= 0.9 * pa_price:
            book = response['item'][0]['subInfo']['ebookList'][0]
            ebook_list.append({
                'itemID' : book['itemId'],
                'isbn' : book['isbn'],
                'priceSales' : book['priceSales'],
                'link' : book['link'],
            })
    except:
        return
    
    return ebook_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
