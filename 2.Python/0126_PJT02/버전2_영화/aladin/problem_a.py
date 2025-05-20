import requests

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

def author_works():
    book_list = []
    response = requests.get(URL, params=params).json()
    
    for book in response['item']:
        book_list.append(book['title'])
    
    return book_list

if __name__ == '__main__':
    print(author_works())
