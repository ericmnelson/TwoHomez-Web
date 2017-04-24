# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Home

# Create your views here.
def index(request):
    featured = Home.objects.all()[0:6]
    context = {
        'featured_list': featured,
        'size_map': [3,3,6,4,3,5],
        'neighborhoods': [n[1] for n in Home.NEIGHBORHOODS],
    }
    return render(request, 'twohomez/index.html', context)

def home_detail(request, home_id):
    house = Home.objects.get(id=int(home_id))
    similar_homes = Home.objects.filter(neighborhood=house.neighborhood,
                                     num_bathrooms=house.num_bathrooms,
                                     num_bedrooms__gte=house.num_bathrooms,
                                     listing_price__lte=(house.listing_price *1.15),
                                     listing_price__gte=(house.listing_price *.85),
                                     )[:3]
    context = {
        'house': house,
        'similar_homes': similar_homes,
        'neighborhoods': [n[1] for n in Home.NEIGHBORHOODS],
    }
    return render(request, 'twohomez/details.html', context)

def search_listings(request):
    city = request.POST.get('city', "San francisco")
    min_price = request.POST.getlist('price-min[]', '0')[0]
    max_price = request.POST.getlist('price-max[]', '100000000')[0]
    min_price = int(min_price.replace("$", "").replace(",", ""))
    max_price = int(max_price.replace("$", "").replace(",", ""))
    neighborhoods_ind = request.POST.getlist('neighborhoods[]', "all")
    if neighborhoods_ind == "all":
        neighborhoods = [n[0] for n in Home.NEIGHBORHOODS]
    else:
        neighborhoods = [Home.NEIGHBORHOODS[int(i)][0] for i in neighborhoods_ind]
    results = Home.objects.all().filter(listing_price__lte=max_price,
                              listing_price__gte=min_price,
                              neighborhood__in=neighborhoods)
    context = {
        "results":results[:10],
        "neighborhoods": [n[1] for n in Home.NEIGHBORHOODS],
    }
    return render(request, 'twohomez/results.html', context)
