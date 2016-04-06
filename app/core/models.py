#encoding: utf-8

from django.db import models



class Maps(models.Model):
	'''
	This class is responsible for mapping the maps table.
	'''
	id_map = models.AutoField(primary_key=True, verbose_name=u'Cod Mapa', db_column='id_map')
	name_map = models.CharField(max_length=200, verbose_name=u'Nome', db_column='name_map', unique=True)
	created_at = models.DateTimeField(verbose_name=u'Data de criação', auto_now_add=True, db_column='date_created')
	updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
	description_map = models.TextField(verbose_name=u'Descrição', db_column='description',blank=True, default='', null=True)

	def __unicode__(self):
		return u'%s' % self.name_map

	def get_short_name(self):
		return self.name_map

	def get_full_name(self):
		return str(self)

	class Meta:
		verbose_name=u'map'
		verbose_name_plural=u'maps'
		ordering=['id_map']
		db_table='maps'


class Routes(models.Model):
	'''
	This class is responsible for mapping the routes table.
	'''
	id_route = models.AutoField(primary_key=True, verbose_name=u'Cod Route', db_column='id_route')
	origin_route = models.CharField(max_length=200, verbose_name=u'Origem', db_column='origin_route')
	destination_route = models.CharField(max_length=200, verbose_name=u'Destino', db_column='destination_route')
	distance_route = models.CharField(max_length=200, verbose_name=u'Distancia', db_column='distance_route')
	created_at = models.DateTimeField(verbose_name=u'Data de criação', auto_now_add=True, db_column='date_created')
	updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
	description_route = models.TextField(verbose_name=u'Descrição', db_column='description',blank=True, default='', null=True)
	id_map = models.ForeignKey(Maps, verbose_name=u'Cod Map', related_name='route_map', on_delete=models.PROTECT)

	def __unicode__(self):
		return u'%s %s %s' % (self.origin_route, self.destination_route, self.distance_route)

	def get_short_name(self):
		return self.id_route

	def get_full_name(self):
		return str(self)

	class Meta:
		verbose_name=u'route'
		verbose_name_plural=u'routes'
		ordering=['id_route']
		unique_together = ('origin_route', 'destination_route', 'id_map')
		db_table='routes'