from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Product

# Create your views here.

def index(request):
    latest_products = Product.objects.order_by('updated')
    template = loader.get_template('products/index.html')
    context = {'latest_products': latest_products}
    return HttpResponse(template.render(context, request))

def detail(request, product_id):
    ''' Return the view for the product detail page. '''
    
