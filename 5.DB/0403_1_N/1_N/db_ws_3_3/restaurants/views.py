from django.shortcuts import render, redirect
from .models import Restaurant, Menu
from .forms import RestaurantForm, MenuForm

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants/index.html', context)

def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurants:detail', restaurant.pk)
    else:
        form = RestaurantForm()
    context = {
        'form': form
    }
    return render(request, 'restaurants/create.html', context)

def detail(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    form = MenuForm()
    menus = restaurant.menu_set.all()
    context = {
        'restaurant': restaurant,
        'form':form,
        'menus':menus,
    }
    return render(request, 'restaurants/detail.html', context)

def create_menu(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    menus = restaurant.menu_set.all()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.restaurant = restaurant
            menu.save()
            return redirect('restaurants:detail', restaurant.pk)
    
    context = {
        'restaurant':restaurant,
        'menus':menus,
        'form':form,
    }
    return render(request, 'restaurants/detail.html', context)