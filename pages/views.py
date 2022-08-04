from django.shortcuts import render
from store.models import Product, ReviewRating
import requests
import http.client
import json

from store.views import search

def index(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    

 
    search = 'iphone 11'
    url = "https://taobao-api.p.rapidapi.com/api"

    querystring = {"api":"item_search","page_size":"40","q":search}

    headers = {
        "X-RapidAPI-Key": "49a092b920msh71f18a68832b06fp18adfajsn2589793aedea",
        "X-RapidAPI-Host": "taobao-api.p.rapidapi.com"
    }

    # response = requests.request("GET", url, headers=headers, params=querystring).json()

    # print(response)  
    
   

    context = {
        'products': products,
        'reviews': reviews,
        # 'response':response
    }
    return render(request, 'pages/index.html', context)



def about(request):
	return render(request, 'pages/about.html')

