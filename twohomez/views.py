# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Home

NEIGHBORHOODS = sorted([n[1] for n in Home.NEIGHBORHOODS])
# Create your views here.
def index(request):
    featured = Home.objects.all().order_by('?')[:6]
    context = {
        'featured_list': featured,
        'size_map': [3,3,6,4,3,5],
        'neighborhoods': NEIGHBORHOODS,
    }
    return render(request, 'twohomez/index.html', context)

def home_detail(request, home_id):
    house = Home.objects.get(id=int(home_id))
    similar_homes = Home.objects.filter(neighborhood=house.neighborhood,
                                     num_bedrooms__gte=house.num_bathrooms,
                                     listing_price__lte=(house.listing_price *1.25),
                                     listing_price__gte=(house.listing_price *.75),
                                     ).exclude(id=int(home_id))[:3]
    fall_avail = int(request.GET.get('fall_avail', "50%").replace("%", ""))
    winter_avail = int(request.GET.get('winter_avail', "50%").replace("%", ""))
    spring_avail = int(request.GET.get('spring_avail', "50%").replace("%", ""))
    summer_avail = int(request.GET.get('summer_avail', "50%").replace("%", ""))
    context = {
        "fall_avail":fall_avail,
        "winter_avail":winter_avail,
        "spring_avail":spring_avail,
        "summer_avail":summer_avail,
        'house': house,
        'house_income': round(house.avg_income_stream(50,50,50,50),2),
        'net_cost': round(house.monthly_mortgage_w_airbnb(50,50,50,50),2),
        'similar_homes': similar_homes,
        'neighborhoods': NEIGHBORHOODS,
    }
    return render(request, 'twohomez/details.html', context)

def search_listings(request):
    city = request.POST.get('city', "San francisco")
    min_price = request.POST.getlist('price-min[]', '0')[0]
    max_price = request.POST.getlist('price-max[]', '100000000')[0]
    min_price = int(min_price.replace("$", "").replace(",", ""))
    max_price = int(max_price.replace("$", "").replace(",", ""))
    fall_avail = int(request.POST.get('fall_avail', "50%").replace("%", ""))
    winter_avail = int(request.POST.get('winter_avail', "50%").replace("%", ""))
    spring_avail = int(request.POST.get('spring_avail', "50%").replace("%", ""))
    summer_avail = int(request.POST.get('summer_avail', "50%").replace("%", ""))
    neighborhoods_ind = request.POST.getlist('neighborhoods[]', "all")
    if neighborhoods_ind == "all":
        neighborhoods = [n[0] for n in Home.NEIGHBORHOODS]
    else:
        neighborhoods = [Home.NEIGHBORHOODS[int(i)][0] for i in neighborhoods_ind]

    results = Home.objects.all().filter(listing_price__lte=max_price,
                              listing_price__gte=min_price,
                              neighborhood__in=neighborhoods)[:25]
    results = sorted(results, key=lambda x: x.monthly_mortgage_w_airbnb(fall_avail,winter_avail, summer_avail, spring_avail))
    mortgages = [round(h.monthly_mortgage_w_airbnb(fall_avail,winter_avail, summer_avail, spring_avail),2) for h in results]
    styles = []
    for m in mortgages:
        if m < 0:
            styles += ["font-weight:bold;color:green;"]
        elif m < h.mortgage/2:
            styles += ["font-weight:bold;color:gold;"]
        else:
            styles += ["font-weight:bold;color:red;"]
    context = {
        "fall_avail":fall_avail,
        "winter_avail":winter_avail,
        "spring_avail":spring_avail,
        "summer_avail":summer_avail,
        "results":results[:25],
        "mortgages":mortgages,
        "styles":styles,
        "neighborhoods": NEIGHBORHOODS,
    }
    return render(request, 'twohomez/results.html', context)


def methodology(request):
    return render(request, 'twohomez/methodology.html', {})
