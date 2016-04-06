from rest_framework import serializers
from core.models import Maps, Routes


class MapsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Maps
		fields = ('id_map', 'name_map', 'created_at', 'updated_at', 'description_map')


class RoutesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Routes
		fields = ('id_route', 'origin_route', 'destination_route', 'distance_route', 'description_route',
				  'created_at','updated_at','id_map')
