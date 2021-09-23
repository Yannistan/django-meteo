from django.test import SimpleTestCase
from django.urls import reverse, resolve
from weather.views import index, delete_city

class TestUrls(SimpleTestCase):
    
    def test_index_url_is_resolved(self):
        url = reverse('home')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, index)    

    def test_delete_city_url_is_resolved(self):
        url = reverse('delete_city', args=['toto_city'])
        self.assertEquals(resolve(url).func, delete_city)
