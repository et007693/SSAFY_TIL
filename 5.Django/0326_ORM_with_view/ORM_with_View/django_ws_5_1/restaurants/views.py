from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request):
    restaurant = Restaurant.objects.all()
    context = {
        'restaurant' : restaurant
    }
    print(context)
    return render(request, 'restaurants/index.html', context)

def new(request):
    return render(request, 'restaurants/new.html')

def create(request):
    data = request.POST
    name = data.get('name')
    description = data.get('detail')
    address = data.get('address')
    phone_number = data.get('phone')
    restaurant = Restaurant(name=name, description=description, address=address, phone_number=phone_number)
    restaurant.save()
    return redirect('restaurants:index')