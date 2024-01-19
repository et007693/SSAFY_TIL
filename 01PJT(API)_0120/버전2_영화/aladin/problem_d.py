import json

def best_book(books):
    title = []
    rate = []

    for book in books:
        id = book['id']
        book_detail = json.load(open(f'data/books/{id}.json', encoding='utf-8'))
        title.append(book_detail['title'])
        rate.append(book_detail['customerReviewRank'])
    best = title[rate.index(max(rate))]

    return best

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
