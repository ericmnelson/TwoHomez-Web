import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
django.setup()

####################################################################

from twohomez.models import Home
import datetime
import numpy as np
import pandas as pd
import requests
import math
from bs4 import BeautifulSoup
from random import randint


def fix_address(addr):
    i = addr.find("St ")
    if i != -1:
        return addr[: i+2] + ".", addr[i+3:]
    i  = addr.find("Ave ")
    if i != -1:
        return addr[: i+3] + ".", addr[i+4:]
    return addr + ".", ""

if __name__ == "__main__":
    print "Deleting all homes"
    Home.objects.all().delete()
    df = pd.read_csv("scripts/data/sf_zillow_apr_23_w_latlon_photo_url_and_nbhrhood.csv")
    for i, row in df.iterrows():
        num_bedrooms = row['bedrooms']
        if math.isnan(num_bedrooms) or num_bedrooms <= 0.5:
            num_bedrooms = 1.0

        num_bathrooms = row['bathrooms']
        if math.isnan(num_bathrooms):
            num_bathrooms = 1.0

        addr_fixed = fix_address(row['address'])
        h, c = Home.objects.get_or_create(
            address0=addr_fixed[0],
            address1=addr_fixed[1],
            city=row['city'],
            state=row['state'],
            zip_code=int(row['zip']),
            listing_price=int(row['price']),
            sale_type=row['sale_type'],
            pic_url=row['photo_url'],
            zillow_url=row['url'],
            latitude=row['latitude'],
            longitude=row['longitude'],
            num_bedrooms=num_bedrooms,
            num_bathrooms=num_bathrooms,
            neighborhood=row['neighborhood'],
            fall_rent_day=randint(150,300),
            winter_rent_day=randint(150,300),
            spring_rent_day=randint(150,300),
            summer_rent_day=randint(150,300),
        )
        h.mortgage = h.monthly_mortgage()
        h.save()
        if i % 25 == 0:
            print "Created number {}".format(i)
