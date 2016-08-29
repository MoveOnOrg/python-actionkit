import re

from django.test import Client, TestCase, override_settings

from actionkit.models import CoreUser

"""
>>> response = c.post('/login/', {'username': 'john', 'password': 'smith'})
>>> response.status_code
>>> response = c.get('/customer/details/')
>>> response.content
b'<!DOCTYPE html...'

assertTrue
assertEqual
assertRedirects
assertContains
https://docs.djangoproject.com/en/1.9/topics/testing/tools/#assertions


"""
TESTSETTINGS = {
    'AK_TEST': True,
    'AK_BASEURL': 'http://localhost/FAKEACTIONKIT',
    'AK_USER': 'foobar',
    'AK_PASSWORD': 'foobar',
    'AK_SECRET': 'fake secret123123',
    'AK_SAVE_MODE': 'api',
}
@override_settings(**TESTSETTINGS)
class APITestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_actionkit_akids(self):
        from actionkit.utils import validate_akid, generate_akid
        from django.conf import settings
        akidcode = generate_akid(settings.AK_SECRET, 'fooo.123123')
        akidusercode = Volunteer.gen_user_akid('123123')
        self.assertTrue(validate_akid(settings.AK_SECRET, akidcode))
        self.assertTrue(validate_akid(settings.AK_SECRET, akidusercode))
        self.assertEqual(generate_akid('mysecret', 'fooo.123123'),
                         'fooo.123123.D07a5p') #hard coded example

