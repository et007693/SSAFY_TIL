import json
from pprint import pprint

def book_info(book, category):
    book_info = {
        'id' : book['id'],
        'name' : book['title'],
        'author' : book['author'],
        'priceSales' : book['priceSales'],
        'description' : book['description'],
        'cover' : book['cover'],
        'categoryName' : book['categoryId'],
        }
    
    cat = []
    for info in book_info['categoryName']:
        for book in category:   
            if book['id'] == info:
                cat.append(book['name'])
            book_info['categoryName'] = cat

    return book_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
