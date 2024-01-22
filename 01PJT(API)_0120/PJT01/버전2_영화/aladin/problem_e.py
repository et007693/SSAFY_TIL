import json

def new_books(books):
    title = []
    year = []
    new = []

    for book in books:
        id = book['id']
        book_detail = json.load(open(f'data/books/{id}.json', encoding='utf-8'))
        title.append(book_detail['title'])
        year.append(int(book_detail['pubDate'][:4]))

    for c, y in enumerate(year):
        if y == 2023:
            new.append(title[c])

    return new

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))