from django.db import models

# Create your models here.
class Deck(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class User(models.Model):
    first_name = models.CharField(max_length=64, null=False, blank = False)
    last_name = models.CharField(max_length=64, null=False, blank = False)
    password = models.CharField(max_length=64, null=False, blank = False)
    confirm_password = models.CharField(max_length=64, null=False, blank = False)
    email = models.CharField(max_length=64, null=False, blank = False)
    phone_number = models.CharField(max_length=64, null=False, blank = False)
    def __str__(self):
        return self.first_name
