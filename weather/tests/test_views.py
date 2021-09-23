from django.test import TestCase
from django.urls import reverse
from weather.models import City


class TestViews(TestCase):
    
    def test_GET(self):
        response = self.client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/weather.html')


    def test_POST_add_new_city(self):
        response = self.client.post(reverse('home') , {'name' : 'Paris'})

        cities = City.objects.all()
        name_list = []

        for i in range(len(cities)):
            name_list.append(cities[i].name)
            
        self.assertEquals(response.status_code, 200)                            
        self.assertIn('Paris', name_list)

    def test_POST_add_already_existent_city(self):
        City.objects.create(name = 'Paris')
        response = self.client.post(reverse('home') , {'name' : 'Paris'})

        cities = City.objects.all()
        name_list = []
        for i in range(len(cities)):
            name_list.append(cities[i].name)
        
        self.assertEquals(response.status_code, 200)
        self.assertIn('Paris', name_list)
        self.assertEquals(len(name_list), 1)

    def test_POST_add_non_existent_city_name(self):
        response = self.client.post(reverse('home'), {'name' : 'false_city'})
        cities = City.objects.all()
        name_list = []
        for i in range(len(cities)):
            name_list.append(cities[i].name)
        self.assertEquals(response.status_code, 200)
        self.assertNotIn('false_city', name_list)

    def test_delete_city(self):
        City.objects.create(name = 'Paris')
        response = self.client.get(reverse('delete_city', args=['Paris']))
        
        self.assertEquals(City.objects.count(), 0)
        self.assertEquals(response.status_code, 302)


    
