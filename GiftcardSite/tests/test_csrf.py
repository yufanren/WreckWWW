from django.test import TestCase, Client
from LegacySite.models import *
from LegacySite.views import *

class Test(TestCase):
  def setup(self):
    self.client = Client()

  def test_csrf(self):
    Product.objects.create(product_name='test', product_image_path='test', recommended_price=0, description='test')

    response = self.client.get('/gift')
    self.assertContains(response, 'csrfmiddlewaretoken')