from django.db import models
from django.contrib.auth.models import User

class iv_item_specification(models.Model):
    name = models.CharField(max_length=64, null=False, blank=True)

    def __str__(self):
        return self.name
class iv_items(models.Model):
    qr=                 models.CharField(max_length=64, null=False, blank=True)
    product_name=       models.CharField(max_length=64, null=False, blank=True)
    quantitity=         models.IntegerField()
    price=              models.IntegerField()
    specification_fk=   models.ForeignKey(iv_item_specification, on_delete=models.CASCADE, null=True , blank=False)

    def __str__(self):
        return self.product_name
class iv_customer(models.Model):
    user=               models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    business_name=      models.CharField(max_length = 32, null=False, blank=True)
    business_email=     models.CharField(max_length = 32, null=False, blank=True)
    business_address=   models.TextField(blank=False, null=True)
    city=               models.CharField(max_length = 32, null=False, blank=True)
    country=            models.CharField(max_length = 32, null=False, blank=True)
    fax=                models.CharField(max_length = 32, null=False, blank=True)

    def __str__(self):
        return self.business_name
class iv_cart(models.Model):
    customer_fk=        models.ForeignKey(iv_customer, on_delete=models.CASCADE, null=True , blank=False)
    item_fk=            models.ForeignKey(iv_items, on_delete=models.CASCADE, null=True , blank=False)
    date_invoice=       models.DateTimeField(editable=False, auto_now=True)
    quantitity=         models.IntegerField()

    def __str__(self):
        return  '%s %s' % (self.item_fk, self.quantitity)
