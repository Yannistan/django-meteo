from django.test import SimpleTestCase
from weather.forms import CityForm


class TestForms(SimpleTestCase):

    def test_form_is_valid(self):
        form = CityForm(data={'name': 'toto_city'})
        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = CityForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
