from dibujos.models import *
from django.http import HttpResponse
import json, os

def alta_artista(request, user, password, nombre, apellidos, correoe, pais, direccion, ciudad, codigopostal, telefono):
	dicc = {}
	try:
		artista = Artista.objects.get(username = user)
	except Artista.DoesNotExist: # Artista no existe y se puede crear
		artista = Artista(username = user, password = password, nombre = nombre,
						  apellidos = apellidos, correoe = correoe, pais = pais, direccion = direccion,
						  codigopostal = codigopostal, telefono = telefono, ciudad = ciudad, activo = 1, 
						  fechacreacion = datetime.datetime.now() + datetime.timedelta(hours = 2),
						  fechaactivacion = datetime.datetime.now() + datetime.timedelta(hours = 2),
						  ultimaaccionfecha = datetime.datetime.now() + datetime.timedelta(hours = 2),
					      ultimoaccesofecha = datetime.datetime.now() + datetime.timedelta(hours = 2),
					      ultimoaccesoip = get_client_ip(request), connect = 1, sesionactiva = 1)
		artista.save()
		dicc = {'content' : 'OK', 'mensaje' : {'username' : user}}
	else: # el usuario ya existe
		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Este artista ya existe'}}
	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def borrar_artista(request, user):
	dicc = {}
	try:
		artista = Artista.objects.get(username = user)
		artista.delete()
		dicc = {'content' : 'OK'}

	except Artista.DoesNotExist: # Artista no existe y no puede ser borrado
		dicc = {'content' : 'KO', 'mensaje' :  'El artista %s no existe.' % user}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def update_artista(request, user, password, nombre, apellidos, correoe, pais, direccion, ciudad, codigopostal, telefono):
	dicc = {}
	try:
		artista = Artista.objects.get(username = user)
		artista.password = password
		artista.nombre = nombre
		artista.apellidos = apellidos
		artista.pais = pais
		artista.codigopostal = codigopostal
		artista.telefono = telefono
		artista.direccion = direccion
		artista.ciudad = ciudad
		artista.correoe = correoe

		artista.save()

		ar = {}
		ar = {'usuario' : artista.username, 'password' : artista.password, 'nombre' : artista.nombre,
		      'apellidos' : artista.apellidos, 'pais' : artista.pais,
		      'codigopostal' : artista.codigopostal, 'telefono' : artista.telefono, 
		      'direccion' : artista.direccion, 'ciudad' : artista.ciudad, 
		      'codartista' : artista.codartista, 'correoe' : artista.correoe}

		dicc = {'content' : 'OK', 'mensaje' : ar}

	except Artista.DoesNotExist:
		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Este artista NO existe'}}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')
c
def borrar_usuario(request, id):
	dicc = {}
	try:
		usuario = Usuario.objects.get(id = id)
		usuario.delete()
		dicc = {'content' : 'OK'}
	except Usuario.DoesNotExist: # Usuario no existe y no puede ser borrado
		dicc = {'content' : 'KO', 'mensaje' :  'El usuario %s no existe.' % user}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def update_usuario(request, idusuario, user, password):
	dicc = {}
	try:
		usuario = Usuario.objects.get(id = idusuario)
		usuario.username = user
		usuario.password = password
		usuario.save()

		us = {}
		us = {'id' : usuario.id, 'username' : usuario.username, 'sesion' : usuario.sesion, 'conectado' : usuario.connect, 'ultimoacceso_ip' : usuario.ultimoaccesoip, 'ultimoaccesofecha' : usuario.ultimoaccesofecha.isoformat(), 'sesionactiva' : usuario.sesionactiva}
		dicc = {'content' : 'OK', 'mensaje' : us}

	except Usuario.DoesNotExist: # Usuario no existe
		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Este usuario NO existe'}}
	
	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')


def alta_usuario(request, user, password):
	dicc = {}
	try:
		usuario = Usuario.objects.get(username = user)
	except Usuario.DoesNotExist: # Usuario no existe y se puede crear
		usuario = Usuario(username = user, password = password, 
					      ultimoaccesofecha = datetime.datetime.now() + datetime.timedelta(hours = 2),
					      ultimoaccesoip = get_client_ip(request), connect = 1, sesionactiva = 1)
		usuario.save()
		dicc = {'content' : 'OK', 'mensaje' : {'username' : user}}
	else: # el usuario ya existe
		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Este usuario ya existe'}}
	
	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')
