from django.contrib import admin
from .models import Contactus,ContactusAdmin,Company,CompanyAdmin,Products,ProductsAdmin,Brands,BrandsAdmin
# Register your models here.

admin.site.register(Contactus,ContactusAdmin),
admin.site.register(Company,CompanyAdmin),
admin.site.register(Products,ProductsAdmin),
admin.site.register(Brands,BrandsAdmin),