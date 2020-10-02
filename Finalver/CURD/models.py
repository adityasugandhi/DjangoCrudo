from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Curd(models.Model):
    name = models.CharField(max_length=60)
    brand_name = models.CharField(max_length=60)
    regular_price_value = models.IntegerField(default=0)
    offer_price_value = models.IntegerField(default=0)
    currency = models.CharField(max_length=10)
    classification_l1 = models.CharField(max_length=20)
    classification_l2 = models.CharField(max_length=20)
    classification_l3 = models.CharField(max_length=20)
    image_url = models,URLField(default=None)

    def __str__(self):
        return self.name
