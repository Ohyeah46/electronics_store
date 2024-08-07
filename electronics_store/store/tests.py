import pytest
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product, Category, Review

from django.test import TestCase
from .models import Category



@pytest.mark.django_db
def test_product_list():
    client = APIClient()
    response = client.get('/api/products/')
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_product_detail():
    product = Product.objects.create(name='Test Product', price=100.00, description='Test Description', category=Category.objects.create(name='Test Category'))
    client = APIClient()
    response = client.get(f'/api/products/{product.id}/')
    assert response.status_code == status.HTTP_200_OK
# Create your tests here.



class CategoryTestCase(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Electronics')
        self.assertEqual(category.name, 'Electronics')