import json

def best_new_books(books):
    title = []
    rate = []
    year = []
    for book in books:
        id = book['id']
        book_detail = json.load(open(f'data/books/{id}.json', encoding='utf-8'))
        if int(book_detail['pubDate'][:4]) == 2023:
            title.append(book_detail['title'])
            rate.append(book_detail['customerReviewRank'])
            year.append(int(book_detail['pubDate'][:4]))

    best = title[rate.index(max(rate))]

    return best

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_new_books(books_list))