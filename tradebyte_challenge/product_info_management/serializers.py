from rest_framework.exceptions import ValidationError

from .models import Category, Article
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parent']

    def validate_parent(self, value):
        if not value:
            raise ValidationError('Parent cannot be null')
        return value


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['sku', 'ean', 'name', 'quantity', 'price', 'categories']
