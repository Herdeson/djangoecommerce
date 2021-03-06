# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from catalog.models import Product
from model_mommy import mommy

class ProductListTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalog:product_list')
        self.client = Client()
        self.products = mommy.make('catalog.Product', _quantity = 10)

    def tearDown(self):
        Product.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTrue('product_list' in response.context)
        product_list = response.context['product_list']
        self.assertEquals(product_list.count(), 2)
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages, 5)

    def test_page_not_fount(self):
        response = self.client.get('{}?page=7'.format(self.url))
        self.assertEquals(response.status_code, 404)
