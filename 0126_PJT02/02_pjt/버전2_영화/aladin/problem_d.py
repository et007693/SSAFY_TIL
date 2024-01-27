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
    'Version' : '20131101'
}

def author_other_works(title):
    book_list = []
    
    params['Query'] = title
    params['QueryType'] = 'title'
    response = requests.get(URL, params=params).json()

    try:
        params['Query'] = response['item'][0]['author'].split('(')[0]
        params['QueryType'] = 'author'
    except:
        return
    
    response = requests.get(URL, params=params).json()
    
    for i in range(5):
        try:
            book_list.append(response['item'][i]['title'])
        except:
            pass
    
    return book_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
