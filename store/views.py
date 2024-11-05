from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Category, Product


def info(request):
	print(request.user.is_authenticated)
	return {'user': request.user}

# Create your views here.
def login(request):
	return render(request, 'store/login.html')

def store(request):
	all_products = Product.objects.all()
	cont = {'all_products': all_products}
	return render(request, 'store/store.html', context=cont)


def categories(request):
	all_categories = Category.objects.all()
	return {'all_categories': all_categories}


def list_category(request, category_slug=None):
	category = get_object_or_404(Category, slug=category_slug)
	products = Product.objects.filter(category=category)
	return render(request, 'store/list-category.html',
				  context={'category': category, 'products': products})


def product_info(request, slug):
	product = get_object_or_404(Product, slug=slug)
	return render(request, 'store/product-info.html', context={'product': product})

def profile(request):
	return render(request, 'store/profile.html')