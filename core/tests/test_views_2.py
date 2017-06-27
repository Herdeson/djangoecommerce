# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):

    def setUp(self):
        #Quando inicia um teste
        client = Client()
        self.url = reverse('index')

    def tearDown(self):
        #Quando terminar o test
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')
