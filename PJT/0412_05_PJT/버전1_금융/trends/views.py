from django.shortcuts import render, redirect
from .forms import KeywordForm
from .models import Keyword, Trend

from bs4 import BeautifulSoup
from selenium import webdriver
import requests

from io import BytesIO
import base64
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

def get_google_data(keyword, year=False):

    if year == True:
        url = f'https://www.google.com/search?q={keyword}&tbs=qdr:y'
    else:
        url = f'https://www.google.com/search?q={keyword}'

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    result_stats = soup.select_one('div#result-stats').text.split('(')[0]
    print(result_stats)
    result = ''
    for s in result_stats:
        if s.isdigit():
            result += s
    return int(result)

# Create your views here.
def keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()
        keywords = Keyword.objects.all()
    context = {
        'form':form,
        'keywords':keywords,
    }
    return render(request, 'trends/keyword.html', context)

def delete(request, pk):
    Keyword.objects.get(pk=pk).delete()
    return redirect('trends:keyword')

def crawling(request):
    keywords = Keyword.objects.all()
    context = {'searchs':[]}
    for keyword in keywords:
        search_result = get_google_data(keyword)
        try:
            trend = Trend.objects.get(name=keyword)
            trend.result = search_result
            trend.save()
            context['searchs'].append(trend)
        except:
            trend = Trend.objects.create(name=keyword, result=search_result, search_period='all')
            context['searchs'].append(trend)
    
    return render(request, 'trends/crawling.html', context)

def histogram(request):
    trends = Trend.objects.all()

    plt.clf()
    plt.figure(figsize=(8,6))
    keyword = []
    result = []
    for trend in trends:
        keyword.append(trend.name)
        result.append(trend.result)

    plt.bar(keyword, result)
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.grid()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    context = {
        'image' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling_histogram.html', context)

def advanced(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        search_result = get_google_data(keyword, year=True)
        try:
            trend = Trend.objects.get(name=keyword)
            trend.result = search_result
            trend.search_period = 'year'
            trend.save()
        except:
            Trend.objects.create(name=keyword, result=search_result, search_period='year')
        
    trends = Trend.objects.filter(search_period='year')

    plt.clf()
    plt.figure(figsize=(8,6))
    keyword = []
    result = []
    for trend in trends:
        keyword.append(trend.name)
        result.append(trend.result)

    plt.bar(keyword, result)
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.grid()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    context = {
        'image' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling_advanced.html', context)