#encoding: utf-8

from django.test import TestCase
from core.models import Maps,Routes

import json


 
class TestApi(TestCase):

	'''
	TestCase Api.
	'''

	def setUp(self):
		self.map = Maps(name_map='SP')
		self.map.save()

		self.route = Routes(origin_route='A', destination_route='B', distance_route='10',id_map=self.map)
		self.route.save()
    
	def tearDown(self): 
		del self.route
		del self.map


	def test_get_price_route(self):	
		url = '/delivery/maps/list'
		pay = {"fuel": "2.50", "origin": "A", "destination": "B","autonomy": "10", "map": "SP"}

		response = self.client.post('/delivery/routes/price_route/', 
										json.dumps(pay),'json')

		self.assertEqual(response.status_code, 201)