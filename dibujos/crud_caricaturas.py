# -*- encoding: utf-8 -*-
from dibujos.models import *
from django.http import HttpResponse
import json, os
import datetime
#bueno

def alta_caricatura(request):
	id_artista_get = request.GET['idartista']
	titulo_get     = request.GET['titulo']
	tag_get		   = request.GET['tag']
	imgAlta_get	   = request.GET['imgalta']
	imgBaja_get	   = request.GET['imgbaja']

	dicc = {}
	try:
		caricatura = Caricaturas.objects.get(idartista = id_artista_get, titulo = titulo_get)
	except Caricaturas.DoesNotExist: # Caricatura no existe y se puede crear

		artista = Artista.objects.get(id = id_artista_get)
		caricatura = Caricaturas(idartista = artista, titulo = titulo_get, tag = tag_get, img_alta = imgAlta_get, 
								 img_miniatura = imgBaja_get, 
								 fechasubida = datetime.datetime.now() + datetime.timedelta(hours = 1),
								 facebook = 0, twitter = 0, googleplus = 0)
		caricatura.save()

		dicc = {'content' : 'OK', 'mensaje' : {'idartista' : caricatura.idartista.id, 'titulo' : titulo_get}}
	else: # la caricatura ya existe
		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Esta caricatura ya existe'}}
	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def caricatura(request):
	id_caricatura = request.GET['idcaricatura']
	dicc = {}
	try:
		caric = Caricaturas.objects.get(id = id_caricatura)
		dicc = {'id' : id_caricatura, 'titulo' : caric.titulo, 'tag' : caric.tag,
				'img_alta' : caric.img_alta, 'img_miniatura' : caric.img_miniatura,
				'fechasubida' : caric.fechasubida.isoformat(), 'facebook' : caric.facebook,
				'twitter' : caric.twitter, 'googleplus' : caric.googleplus, 
				'whatsapp' : caric.whatsapp, 'visualizaciones' : caric.visualizaciones}
		
	except Caricaturas.DoesNotExist:
		dicc = {'content' : 'KO', 'error' : 'La caricatura con este id : %s, no existe' % id_caricatura}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def caricaturas(request):
		
	usuario = request.GET['idartista']
	dicc = []
	diccs = {}
	try:
		if usuario == 'todos':
			carics = Caricaturas.objects.all().order_by('id')
		else:
			carics = Caricaturas.objects.filter(idartista = usuario)

		for caric in carics:
			dicc.append({'id' : caric.id, 'titulo' : caric.titulo, 'tag' : caric.tag,
					'img_alta' : caric.img_alta, 'img_miniatura' : caric.img_miniatura,
					'fechasubida' : caric.fechasubida.isoformat(), 'facebook' : caric.facebook,
					'twitter' : caric.twitter, 'googleplus' : caric.googleplus, 
					'whatsapp' : caric.whatsapp, 'visualizaciones' : caric.visualizaciones})

		diccs = {'content' : 'ok', 'caricaturas' : dicc}
	except Caricaturas.DoesNotExist:
		diccs = {'content' : 'ko'}
	
	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(diccs))
	return HttpResponse(data, 'application/json')


def borrar_caricatura(request):
	id_artista    = request.GET['idartista']
	id_caricatura = request.GET['idcaricatura']

	dicc = {}
	try:
		artista = Artista.objects.get(id = id_artista)
	except Artista.DoesNotExist: #No existe el artista -> improbable
		dicc = {'content' : 'KO', 'mensaje' : 'El artista con id = %s no esta en la BDD.' % id_artista}
		data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
		return HttpResponse(data, 'application/json')
		
	try:
		caricatura = Caricaturas.objects.get(idartista = id_artista, id = id_caricatura)
		caricatura.delete()
		dicc = {'content' : 'OK'}

	except Caricaturas.DoesNotExist: # Caricatura no existe y no puede ser borrado
		dicc = {'content' : 'KO', 'mensaje' :  'La caricatura con id %s del artista %s %s no existe.' % (id_caricatura, artista.nombre, artista.apellidos )}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def update_caricatura(request):
	idartista_get 		 = request.GET['idartista']
	titulo_get 			 = request.GET['titulo']
	nuevo_titulo_get	 = request.GET['nuevo_titulo']
	tag_get 			 = request.GET['tag']
	img_alta_get		 = request.GET['img_alta']
	img_baja_get 		 = request.GET['img_baja']

	dicc = {}
	try:
		artista = Artista.objects.get(id = idartista_get)
		caricatura = Caricaturas.objects.get(idartista = artista, titulo = titulo_get)
		caricatura.titulo = nuevo_titulo_get
		caricatura.tag = tag_get
		caricatura.img_alta = img_alta_get
		caricatura.img_miniatura = img_baja_get

		caricatura.save()

		datos = {'titulo' : caricatura.titulo, 'tag' : caricatura.tag, 'img_alta' : caricatura.img_alta, 'img_miniatura' : caricatura.img_miniatura}
		dicc = {'content' : 'OK', 'mensaje' : json.dumps(datos)}

	except Caricaturas.DoesNotExist:
		dicc = {'content' : 'KO', 'mensaje' : 'Caricatura no existe'}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

