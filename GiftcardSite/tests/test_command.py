from json import JSONDecodeError
from django.test import TestCase, Client
from io import StringIO
from LegacySite.models import *
from LegacySite.views import *
import sys

class Test(TestCase):
  def setup(self):
    self.client = Client()

  def test_command(self):
    pw = 'admins_password'
    user = User.objects.create(username='admin', password=pw)
    filename = 'tests/command_injection.gftcrd'
    self.client.force_login(user)

    sys.stdout = mystdout = StringIO()

    with open(filename) as fp:
      try:
        self.client.post('/use.html', data={'card_supplied': True, 'card_fname': '1;echo "Hacked!";giftcardreader 2', 'card_data': fp})
      except JSONDecodeError:
        pass
    sys.stdout = sys.__stdout__
    assert 'Hacked!' not in mystdout.getvalue()