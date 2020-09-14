from django.db import models

# Create your models here.

def get_upper_level_parent():
    # Todo implement
    raise Exception
    return

class Category(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET(get_upper_level_parent))


class Article(models.Model):
    categories = models.ManyToManyField('Category', related_name='articles', blank=True, null=True)
    sku = models.CharField(max_length=128)
    ean = models.CharField(max_length=128)
    name = models.CharField(max_length=1024)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()
