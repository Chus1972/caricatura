from dibujos.models import *
from django.http import HttpResponse
import json, os
import datetime

def alta_caricatura(request, idArtista, titulo, tag, imgAlta, imgBaja):
	dicc = {}
	try:
		caricatura = Caricaturas.objects.get(idartista = idArtista, titulo = titulo)
	except Caricaturas.DoesNotExist: # Caricatura no existe y se puede crear

		artista = Artista.objects.get(id = idArtista)
		caricatura = Caricaturas(idartista = artista, titulo = titulo, tag = tag, img_alta = imgAlta, 
								 img_miniatura = imgBaja, 
								 fechasubida = datetime.datetime.now() + datetime.timedelta(hours = 2),
								 facebook = 0, twitter = 0, googleplus = 0)
		print 'por aqui pasa'
		caricatura.save()

		dicc = {'content' : 'OK', 'mensaje' : {'idartista' : caricatura.idartista.id, 'titulo' : titulo}}
	else: # la caricatura ya existe
		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Esta caricatura ya existe'}}
	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def caricatura(request, idcaricatura):
	dicc = {}
	try:
		caric = Caricaturas.objects.get(id = idcaricatura)
		dicc = {'id' : idcaricatura, 'titulo' : caric.titulo, 'tag' : caric.tag,
				'img_alta' : caric.img_alta, 'img_miniatura' : caric.img_miniatura,
				'fechasubida' : caric.fechasubida.isoformat(), 'facebook' : caric.facebook,
				'twitter' : caric.twitter, 'googleplus' : caric.googleplus, 
				'whatsapp' : caric.whatsapp, 'visualizaciones' : caric.visualizaciones}
		
	except Exception as e:
		dicc = {'content' : 'KO', 'error' : e}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')


def borrar_caricatura(request, idartista, titulo):
	dicc = {}
	try:
		artista = Artista.objects.get(id = idartista)
		caricatura = Caricaturas.objects.get(idartista = artista, titulo = titulo)
		caricatura.delete()
		dicc = {'content' : 'OK'}

	except Caricaturas.DoesNotExist: # Caricatura no existe y no puede ser borrado
		artista = Artista.objects.get(id = idartista)
		dicc = {'content' : 'KO', 'mensaje' :  'La caricatura %s del artista %s %s no existe.' % (titulo, artista.nombre, artista.apellidos )}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def update_caricatura(request, idartista, titulo, nuevo_titulo, tag, img_alta, img_miniatura):
	dicc = {}
	try:
		artista = Artista.objects.get(id = idartista)
		caricatura = Caricaturas.objects.get(idartista = artista, titulo = titulo)
		caricatura.titulo = nuevo_titulo
		caricatura.tag = tag
		caricatura.img_alta = img_alta
		caricatura.img_miniatura = img_miniatura

		caricatura.save()
		dicc = {'content' : 'OK'}

	except Caricaturas.DoesNotExist:
		dicc = {'content' : 'KO', 'mensaje' : 'Caricatura no existe'}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

