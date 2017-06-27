from django.test import TestCase
from django.core.urlresolvers import reverse

from catalog.models import Category, Product
from model_mommy import mommy


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = mommy.make('catalog.Category')

    def test_get_absolute_url(self):
        self.assertEquals(self.category.get_absolute_url(), reverse( 'catalog:category', kwargs={'slug': self.category.slug }))

class ProductTestCase(TestCase):
    def setUp(self):
        self.product =mommy.make('catalog.Product')

    def test_get_absolute_url(self):
        self.assertEquals(self.product.get_absolute_url, reverse('catalog:product', kwargs={'slug': self.product.slug }))
