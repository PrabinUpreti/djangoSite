from django.contrib import admin
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discounts')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stocks')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)

