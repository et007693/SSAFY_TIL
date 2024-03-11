import requests
from pprint import pprint

URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

params = {
    'ttbkey' : 'ttbthdckddyd1231146001',
    'Query' : '파울로 코엘료',
    'QueryType' : 'Author',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101'
}

def bestseller_book():
    # 여기에 코드를 작성합니다.
    salespoint = []
    book_list = []
    
    response = requests.get(URL, params=params).json()

    for book in response['item']:
        salespoint.append(book['salesPoint'])
    
    point = sorted(salespoint, reverse=True)[4]
    for book in response['item']:
        if book['salesPoint'] >= point:
            book_list.append(book['title'])

    return book_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(bestseller_book())
