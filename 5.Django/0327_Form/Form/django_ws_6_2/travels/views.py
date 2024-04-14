from django.shortcuts import render, redirect
from .models import Travel
from .forms import Travelform

# Create your views here.
def index(request):
    travels = Travel.objects.all()
    context = {
        'travels':travels
    }
    return render(request, 'travel/index.html', context)

def create(request):
    if request.method == "POST":
        form = Travelform(request.POST)
        if form.is_valid():
            travel = form.save()
            return redirect('travel:detail', travel.pk)
    else:
        form = Travelform()
    context = {
        'form':form
    }
    return render(request, 'travel/create.html', context)

def detail(request, pk):
    travel = Travel.objects.get(pk=pk)
    context = {
        'travel':travel
    }
    return render(request, 'travel/detail.html', context)

def delete(request, pk):
    travel = Travel.objects.get(pk=pk)
    travel.delete()
    return redirect('travel:index')