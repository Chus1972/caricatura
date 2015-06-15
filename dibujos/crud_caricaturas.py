from dibujos.models import *
from django.http import HttpResponse
import json, os

def alta_caricatura(request, idArtista, titulo, tag, imgAlta, imgBaja, facebook, twitter, googleplus):
	dicc = {}
	try:
		caricatura = Caricaturas.objects.get(idArtista = idArtista, titulo = titulo)
	except Caricaturas.DoesNotExist: # Caricatura no existe y se puede crear
		print 'entra en except'
		caricatura = Caricaturas(idartista = idartista, titulo = titulo, tag = tag, img_alta = imgAlta, img_miniatura = imgBaja,
								 fecha_subida = datetime.datetime.now() + datetime.timedelta(hours = 2),
						 	     facebook = facebook, twitter = twitter, googleplus = googleplus, visualizaciones = 0)
		caricatura.save()
		print 'grabado'
		dicc = {'content' : 'OK', 'mensaje' : {'idArtista' : idartista, 'titulo' : titulo, 'imgAlta' : imgAlta, 'imgBaja' : imgBaja}}
	else: # el usuario ya existe
		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Esta caricatura ya existe'}}
	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def borrar_caricatura(request, idArtista, titulo):
	dicc = {}
	try:
		caricatura = Caricaturas.objects.get(idArtista = idArtista, titulo = titulo)
		caricatura.delete()
		dicc = {'content' : 'OK'}

	except Caricaturas.DoesNotExist: # Caricatura no existe y no puede ser borrada
		dicc = {'content' : 'KO', 'mensaje' :  'La caricatura %s del artista %s no existe.' % (titulo, idArtista))}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')



