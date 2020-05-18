from datetime import datetime
from django.db import models


# Create your models here.
class Contact(models.Model):
    listing = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
