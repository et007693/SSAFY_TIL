from django.shortcuts import render, redirect
from .models import Store
from .forms import CreationFrom, ProductForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)

def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    products = store.product_set.all()
    form = ProductForm()
    context = {
        'store': store,
        'form':form,
        'products':products
    }
    return render(request, 'stores/detail.html', context)

def create(request):
    if request.method == "POST":
        form = CreationFrom(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect('stores:detail', store.pk)
        
    else:
        form = CreationFrom()
    context = {
        'form':form
    }
    return render(request, 'stores/create.html', context)

def product(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    product = store.product_set.all()
    form = ProductForm(request.POST)
    print('ture')
    if form.is_valid():
        print('valid')
        product = form.save(commit=False)
        product.user = request.user
        product.store = store
        product.save()
        return redirect('stores:detail', store_pk)
    print('end')
    context = {
        'store':store,
        'product':product,
        'form':form
    }
    return render(request, 'stores/detail.html', context)