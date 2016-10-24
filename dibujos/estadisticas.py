# -*- encoding: utf-8 -*-
from dibujos.models import *
from django.http import HttpResponse
import json, os

def visualizacion_mas_1(request):
	id_caricatura = request.GET['idcaricatura']
	print id_caricatura
	dicc = {}
	
	try:
		caric = Caricaturas.objects.get(id = id_caricatura)
		print caric.visualizaciones
	except Caricaturas.DoesNotExist:
		dicc = {'content' : 'KO', 'mensaje' : 'La caricatura con id %s  no existe ' % id_caricatura}
		data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
		
		return HttpResponse(data, 'application/json')

	caric.visualizaciones += 1
	caric.save()

	dicc = {'content' : 'OK', 'visualizaciones' : caric.visualizaciones}
	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))

	return HttpResponse(data, 'application/json')
