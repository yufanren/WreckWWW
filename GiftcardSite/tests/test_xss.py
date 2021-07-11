from django.test import TestCase, Client
from LegacySite.models import *
from LegacySite.views import *

class Test(TestCase):
  def setup(self):
    self.client = Client()

  def test_xss(self):
    Product.objects.create(product_name='test', product_image_path='test', recommended_price=0, description='test')

    response = self.client.get('/gift', {'director':'<a>Hacked!</a>'})
    self.assertContains(response, "&lt;a&gt;Hacked!&lt;/a&gt;", status_code=200)

    response = self.client.get('/buy', {'director':'<a>Hacked!</a>'})
    self.assertContains(response, "&lt;a&gt;Hacked!&lt;/a&gt;", status_code=200)

