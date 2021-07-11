from django.test import TestCase, Client
from LegacySite.models import *
from LegacySite.views import *

class Test(TestCase):
  def setup(self):
    self.client = Client()

  def test_csrf(self):
    pw = 'admins_password'
    user = User.objects.create(username='admin', password=pw)
    filename = 'tests/sql_injection.gftcrd'
    self.client.force_login(user)

    with open(filename) as fp:
      response = self.client.post('/use.html', data={'card_supplied': True, 'card_fname': 'test', 'card_data': fp})
      self.assertNotContains(response, pw)