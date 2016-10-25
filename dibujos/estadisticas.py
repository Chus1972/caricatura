# -*- encoding: utf-8 -*-
from dibujos.models import *
from django.http import HttpResponse
import json, os


def redes_mas_1(request):
	if request.GET.get('idcaricatura'):
		id_caricatura = request.GET['idcaricatura']

	if request.GET.get('mascara_red'):
		mascarared = request.GET['mascara_red']
	else:
		mascarared = 0

	mascara = list(map(int, str(mascarared)))

	dicc = {}
	
	try:
		caric = Caricaturas.objects.get(id = id_caricatura)
	except Caricaturas.DoesNotExist:
		dicc = {'content' : 'KO', 'mensaje' : 'La caricatura con id %s  no existe ' % id_caricatura}
		data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
		
		return HttpResponse(data, 'application/json')


	if mascara[0] == 1:
		caric.visualizaciones += 1
	if mascara[1] == 1:
		caric.facebook +=1
	if mascara[2] == 1:
		caric.twitter +=1
	if mascara[3] == 1:
		caric.googleplus +=1
	if mascara[4] == 1:
		caric.whatsapp +=1

	caric.save()

	dicc = {'content' : 'OK', 'visualizaciones' : caric.visualizaciones, 'facebook' : caric.facebook, 'twitter' : caric.twitter, 'googleplus' : caric.googleplus, 'whatsapp' : caric.whatsapp}
	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))

	return HttpResponse(data, 'application/json')

