from django.shortcuts import render
import requests
from pprint import pprint

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'key'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def api_data(request):
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = 'ttbthdckddyd1231146001'
    params = {
        'ttbkey': API_KEY,
        'QueryType' : 'ItemNewSpecial',
        'SearchTarget' : 'Book',
        'Version' : '20131101',
        'Output' : 'JS',
        'MaxResults' : 50
    }

    data = requests.get(API_URL, params=params).json()
    result = []

    for b in data['item']:
        result.append({
            '국제 표준 도서 번호' : b['isbn'],
            '저자' : b['author'],
            '제목' : b['title'],
            '출간일' : b['pubDate'],
        })

    context = {
        'result' : result
    }

    return render(request, 'book.html', context)