from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class product_category(models.Model):
    title = models.CharField(max_length=32, null=False, blank=True)
    def __str__(self):
        return self.title

class product_type(models.Model):
    title = models.CharField(max_length=32, null=False, blank=True)
    category_id = models.ForeignKey(product_category, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s' % (self.title, self.category_id.title)

class product(models.Model):
    name = models.CharField(max_length=32, null=False, blank=True)
    product_type_id = models.ForeignKey(product_type, on_delete=models.CASCADE)
    desc_qtty = models.IntegerField(default=3,validators=[MaxValueValidator(7), MinValueValidator(3)])
    def __str__(self):
        return '%s %s %s' % (self.name, self.product_type_id.category_id.title, self.product_type_id.title)

class product_option(models.Model):
    name_id = models.ForeignKey(product, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='prod_img', blank=True)
    def __str__(self):
        return '%s %s %s' % (self.name_id.product_type_id.title, self.name_id.name, self.price)
class product_attribute(models.Model):
    name = models.CharField(max_length=32, null=False, blank=True)
    def __str__(self):
        return self.name
class product_description(models.Model):
    product_option_id = models.ForeignKey(product_option, on_delete=models.CASCADE)
    product_attribute_id = models.ForeignKey(product_attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=32, null=False, blank=True)
    def __str__(self):
        return '%s %s' % (self.product_option_id.name_id.name, self.product_attribute_id.name)

class customer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=32, null=False, blank=True)
    def __str__(self):
        return '%s %s' % (self.user_id.username, self.phone)
