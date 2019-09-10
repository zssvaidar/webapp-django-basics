from django.contrib import admin
from .models import iv_customer, iv_items, iv_item_specification, iv_cart

from django.contrib import admin
admin.site.register(iv_customer)
admin.site.register(iv_items)
admin.site.register(iv_item_specification)
admin.site.register(iv_cart)
