import requests
from pprint import pprint

URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

params = {
    'Query' : '파울로 코엘료',
    'QueryType' : 'Author',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101'
}

def bestseller_book():
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

if __name__ == '__main__':
    pprint(bestseller_book())
