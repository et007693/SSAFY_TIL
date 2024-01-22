import json

def sorted_cs_books_by_price(books, categories):
    title = []
    price = []
    sorted_title = []

    for book in books:
        id = book['id']
        book_detail = json.load(open(f'data/books/{id}.json', encoding='utf-8'))
        cat = []
        for cid in book['categoryId']:
            for category in categories:
                if category['id'] == cid:
                    cat.append(category['name'])
                book['categoryId'] = cat
                
        if '컴퓨터 공학' in book['categoryId']:
            title.append(book_detail['title'])
            price.append(int(book_detail['priceSales']))

    sorted_price = sorted(range(len(price)), key=lambda k: price[k])
    for index in sorted_price:
        sorted_title.append(title[index])
    
    print(sorted_price)
    return sorted_title

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))