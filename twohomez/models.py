# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Home(models.Model):
    address0 = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    listing_price = models.PositiveIntegerField()
    pic_url = models.CharField(max_length=200, null=True)
    zillow_url = models.CharField(max_length=200, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    num_bedrooms = models.FloatField()
    num_bathrooms = models.FloatField()
    sale_type = models.CharField(max_length=200, null=True)
    NEIGHBORHOODS = (
        ('Seacliff', 'Seacliff'),
        ('Haight Ashbury', 'Haight Ashbury'),
        ('Outer Mission', 'Outer Mission'),
        ('Downtown/Civic Center', 'Civic Center'),
        ('Diamond Heights', 'Diamond Heights'),
        ('Lakeshore', 'Lakeshore'),
        ('Russian Hill', 'Russian Hill'),
        ('Noe Valley', 'Noe Valley'),
        ('Inner Sunset', 'Inner Sunset'),
        ('Treasure Island/YBI', 'Treasure Island'),
        ('Outer Richmond', 'Outer Richmond'),
        ('Crocker Amazon', 'Crocker Amazon'),
        ('Excelsior', 'Excelsior'),
        ('Parkside', 'Parkside'),
        ('Financial District', 'Financial District'),
        ('Ocean View', 'Ocean View'),
        ('Mission', 'Mission'),
        ('West of Twin Peaks', 'West of Twin Peaks'),
        ('Inner Richmond', 'Inner Richmond'),
        ('Marina', 'Marina'),
        ('Bayview', 'Bayview'),
        ('Visitacion Valley', 'Visitacion Valley'),
        ('Pacific Heights', 'Pacific Heights'),
        ('Presidio Heights', 'Presidio Heights'),
        ('South of Market', 'SoMa'),
        ('Glen Park', 'Glen Park'),
        ('Potrero Hill', 'Potrero Hill'),
        ('Castro/Upper Market', 'Castro/Upper Market'),
        ('Twin Peaks', 'Twin Peaks'),
        ('Bernal Heights', 'Bernal Heights'),
        ('Chinatown', 'Chinatown'),
        ('North Beach', 'North Beach'),
        ('Presidio', 'Presidio'),
        ('Nob Hill', 'Nob Hill'),
        ('Outer Sunset', 'Outer Sunset'),
        ('Western Addition', 'Western Addition'),
        ('Golden Gate Park', 'Golden Gate Park'),
    )
    neighborhood = models.CharField(max_length=30, choices=NEIGHBORHOODS)
    mortgage = models.FloatField(null=True)
    fall_rent_day = models.FloatField(null=True)
    winter_rent_day = models.FloatField(null=True)
    spring_rent_day = models.FloatField(null=True)
    summer_rent_day = models.FloatField(null=True)

    def monthly_mortgage(self):
        L = 0.8 * self.listing_price
        c = .0412/12
        n = 30 * 12
        return (L * (c * ((1 + c)**n))) / (((1 + c)** n) - 1)

    def avg_income_stream(self, fall_avail, winter_avail, spring_avail, summer_avail):
        fall_income = fall_avail/100.0 * self.fall_rent_day * 30.5 * 3
        winter_income = winter_avail/100.0 * self.winter_rent_day * 30.5 * 3
        spring_income = spring_avail/100.0 * self.spring_rent_day * 30.5 * 3
        summer_income = summer_avail/100.0 * self.summer_rent_day * 30.5 * 3
        total_income = fall_income + winter_income + spring_income + summer_income
        return total_income/12.0

    def monthly_mortgage_w_airbnb(self, fall_avail, winter_avail, spring_avail, summer_avail):
        return self.mortgage - self.avg_income_stream(fall_avail, winter_avail, spring_avail, summer_avail)

    def __str__(self):
        return "{} {} {}, {}".format(self.address0, self.address1, self.city, self.state)
