from django.db import models
from django.contrib.auth.models import User

class iv_item_specification(models.Model):
    name = models.CharField(max_length=64, null=False, blank=True)

    def __str__(self):
        return self.name
