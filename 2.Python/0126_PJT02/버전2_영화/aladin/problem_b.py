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

def best_review_books():
    book_list = []
    response = requests.get(URL, params=params).json()

    for book in response['item']:
        if book['customerReviewRank'] >= 9:
            book_list.append(book)

    return book_list


if __name__ == '__main__':
    pprint(best_review_books())
