from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

data = pd.read_csv('C:/Users/SSAFY/Desktop/04-pjt/버전1_금융/weathers/data/austin_weather.csv')
data['Date'] = pd.to_datetime(data['Date'])

data2 = pd.read_csv('C:/Users/SSAFY/Desktop/04-pjt/버전1_금융/weathers/data/austin_weather.csv')

# Create your views here.
def problem1(request):
    print(data['Date'])
    context = {
        'data':data2
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    plt.clf()
    plt.figure(figsize=(8,6))

    plt.plot('Date', 'TempHighF', data=data)
    plt.plot('Date', 'TempAvgF', data=data)
    plt.plot('Date', 'TempLowF', data=data)

    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend(('High Temperature', 'Average Temperature','Low Temperature'))
    plt.grid()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('/n', '')
    buffer.close()
    context = {
        'image' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    monthly_avg = data.groupby(data['Date'].dt.strftime('%Y-%m'))
    total_len = len(monthly_avg)

    plt.clf()
    plt.figure(figsize=(8,6))

    plt.plot(monthly_avg['TempHighF'].mean())
    plt.plot(monthly_avg['TempAvgF'].mean())
    plt.plot(monthly_avg['TempLowF'].mean())

    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.xticks(np.arange(1, total_len, 6))
    plt.legend(('High Temperature','Average Temperature','Low Temperature'), loc='lower right')
    plt.grid()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('/n', '')
    buffer.close()
    context = {
        'image' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem3.html', context)

def problem4(request):
    events = data['Events'].str.split(' , ', expand=True).stack().reset_index(level=0, drop=True)
    event_counts = events.value_counts().reset_index()
    event_counts.iloc[0,0] = 'No Events'

    plt.clf()
    plt.figure(figsize=(8,6))

    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.bar(event_counts['index'],event_counts['count'])
    plt.grid()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('/n', '')
    buffer.close()
    context = {
        'image' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem4.html', context)