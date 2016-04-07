#encoding: utf-8

from django.test import TestCase
from core.models import Maps,Routes



class TestModelMaps(TestCase):

    '''
    TestCase Model Maps.
    '''

    def setUp(self):
        self.map = Maps.objects.get_or_create(name_map='SP')
     
    def tearDown(self): 
        del self.map

    def test_created_map(self):
        self.assertEqual(Maps.objects.count(), 1)



class TesteModelRoute(TestCase):
    
    '''
    TestCase Model Routes.
    '''

    def setUp(self):
        self.maps = Maps(name_map='SP')
        self.maps.save()
        self.route = Routes.objects.get_or_create(origin_route='A', destination_route='B', distance_route='10',id_map=self.maps)

    def tearDown(self):
        del self.route
        del self.maps

    def test_created_route(self):
        self.assertEqual(Maps.objects.count(), 1)