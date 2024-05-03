from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import pandas as pd

array_length = 1000
random_range = 5000


@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)

def dataframe(request):
    data = pd.read_csv('./data/test_data.csv', encoding='cp949')
    data = data.to_dict('records')
    json_data = {'data': data}

    return JsonResponse(json_data, json_dumps_params={'ensure_ascii': False, 'indent':4})

def fillna(request):
    data = pd.read_csv('./data/test_data.csv', encoding='cp949')
    data.fillna('NULL', inplace=True)
    data = data.to_dict('records')
    json_data = {'data': data}

    return JsonResponse(json_data, json_dumps_params={'ensure_ascii': False, 'indent':4})

def age(request):
    data = pd.read_csv('./data/test_data.csv', encoding='cp949')
    mean_age = data['나이'].mean()
    data['age_diff'] = abs(data['나이'] - mean_age)
    df_sorted = data.sort_values('age_diff')

    similar_rows = df_sorted.head(10).drop(columns=['age_diff'])
    similar_rows = similar_rows.to_dict('records')
    json_data = {'data': similar_rows}

    return JsonResponse(json_data, json_dumps_params={'ensure_ascii': False, 'indent':4})

