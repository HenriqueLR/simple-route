#encoding> utf-8

from core.models import Maps, Routes
from core.serializers import MapsSerializer, RoutesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import json
from seek.utils import RoutePrice


class MapsList(APIView):
    """
    List all Maps, or create a new Map.
    """
    def get(self, request, format=None):
        maps = Maps.objects.all()
        serializer = MapsSerializer(maps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        maps = MapsSerializer(data=request.data)
        if maps.is_valid():
            maps.save()
            return Response(maps.data, status=status.HTTP_201_CREATED)
        return Response(maps.errors, status=status.HTTP_400_BAD_REQUEST)


class MapsCustom(APIView):
	"""
	Retrieve, update or delete a maps instance.
	"""
	def get_object(self, string):
		try:
			return Maps.objects.get(name_map=string)
		except Maps.DoesNotExist:
			raise Http404

	def get(self, request, string, format=None):
		maps = self.get_object(string)
		serializer = MapsSerializer(maps)
		return Response(serializer.data)

	def put(self, request, string, format=None):
		maps = self.get_object(string)
		serializer = MapsSerializer(maps, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, string, format=None):
		maps = self.get_object(string)
		maps.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class RoutesList(APIView):
	"""
	List all Routes, or create a new Route.
	"""
	def get(self, request, format=None):
		routes = Routes.objects.all()
		serializer = RoutesSerializer(routes, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		routes = RoutesSerializer(data=request.data)
		if routes.is_valid():
			routes.save()
			return Response(routes.data, status=status.HTTP_201_CREATED)
		return Response(routes.errors, status=status.HTTP_400_BAD_REQUEST)		                


class RoutesCustomName(APIView):
	"""
	Retrieve, update or delete a routes instance.
	"""
	def get_object(self, pk):
		try:
			return Routes.objects.get(id_route=(pk))
		except Routes.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		routes = self.get_object(pk)
		serializer = RoutesSerializer(routes)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		routes = self.get_object(pk)
		serializer = RoutesSerializer(routes, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		name = self.get_object(pk)
		name.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
 


def price_route(request):
	"""
	Get route information.
	"""
	if request.method == 'POST':
		received_json_data = json.loads(request.body)

		fuel  = float(received_json_data['fuel'])
		origin  = received_json_data['origin']
		destination  = received_json_data['destination']
		autonomy  = float(received_json_data['autonomy'])
		map_data  = received_json_data['map']
	
		routes = Routes.objects.filter(id_map__name_map=(map_data))
		
		route_price = RoutePrice(routes)
		route_price = route_price.calc(origin, destination)

		if(route_price!=None):
			distance = float(route_price['distance'])
			routes = route_price['routes']
			price = (distance / autonomy) * fuel
			result = {'routes': routes, 'distance': distance, 'price': price}
			return HttpResponse(json.dumps(result), content_type='application/json',status=201)
		error = {"error":"Mapa pesquisado nao existe."}	
		return HttpResponse(json.dumps(error), content_type='application/json')