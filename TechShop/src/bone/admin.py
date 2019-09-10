from django.contrib  import admin
from . models import product_category, product_type, product, product_option, product_attribute, product_description

admin.site.register(product_category)
admin.site.register(product_type)
admin.site.register(product)
admin.site.register(product_option)
admin.site.register(product_attribute)
admin.site.register(product_description)
# admin.site.register(profile_invoice)
