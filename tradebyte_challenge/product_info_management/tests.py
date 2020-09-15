from django.test import TestCase

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from .models import Category

# Create your tests here.


class CategoryViewsetTests(TestCase):

    def setUp(self):
        root = Category.objects.filter(parent__isnull=True).first()
        self.category1 = Category.objects.create('category 1', parent=root)
        self.category2 = Category.objects.create('category 2', parent=self.category1)
        self.factory = APIRequestFactory()

    def test_delete_root(self):
        root = Category.objects.filter(parent__isnull=True).first()
        request = factory.delete('/categories/' + str(root.pk))
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_parent(self):
        request = factory.delete('/categories/' + str(self.category1.pk))
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        category = Category.objects.filter(pk=self.category1.pk)
        self.assertFalse(category.exists())
        category_2 = Category.objects.filter(pk=self.category2.pk)
        self.assertEqual(category_2.parent_id, self.category1.parent_id)
