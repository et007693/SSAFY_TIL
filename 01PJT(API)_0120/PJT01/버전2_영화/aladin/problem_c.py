import json
from pprint import pprint

def books_info(books, category):
    books_info = []
    for book in books:
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

        books_info.append(book_info)

    return books_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
