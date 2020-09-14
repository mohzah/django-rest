from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.DO_NOTHING)

    @property
    def is_root(self):
        return self.parent is None

    def delete(self, using=None, keep_parents=False):
        Category.objects.filter(parent=self).update(parent_id=self.parent_id)
        super(Category, self).delete(using, keep_parents)

    def __str__(self):
        return f'{self.id} {self.name}'


class Article(models.Model):
    categories = models.ManyToManyField('Category', related_name='articles', blank=True, null=True)
    sku = models.CharField(max_length=128, unique=True, verbose_name='SKU')
    ean = models.CharField(max_length=128, unique=True, verbose_name='EAN')
    name = models.CharField(max_length=1024)
    quantity = models.IntegerField(default=0, help_text='Defaults to 0')
    price = models.FloatField()
    # currency = models.CharField(max_length=32, choices=['USD', 'Euro'])
