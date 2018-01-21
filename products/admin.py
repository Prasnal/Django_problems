from django.contrib import admin
from .models import Product,Company,Country,Country_Products

admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Country_Products)
#admin.site.register(Country)

