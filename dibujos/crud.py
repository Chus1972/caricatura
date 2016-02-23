from dibujos.models import *
from django.http import HttpResponse
import json, os, datetime
#from django.views.decorators.csrf import csrf_protect

def alta_artista(request):
	dicc = {}
	try:
		artista = Artista.objects.get(username = request.POST['user'], password = request.POST['password'])
	except Artista.DoesNotExist: # Artista no existe y se puede crear
		artista = Artista(username = request.POST['user'], password = request.POST['password'], nombre = request.POST['nombre'],
						  apellidos = request.POST['apellidos'], tipousuario = request.POST['tipoususario'], 
						  correoe = request.POST['email'], pais = request.POST['pais'], 
						  direccion = request.POST['direccion'], codigopostal = request.POST['codigopostal'], 
						  telefono = request.POST['telefono'], ciudad = request.POST['ciudad'], activo = 1, 
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

#def alta_artista2(request, user, password, nombre, apellidos,  pais, direccion, ciudad, codigopostal, telefono):
#	dicc = {}
#	print "email : " + request.GET['email']
#	try:
#		artista = Artista.objects.get(username = user)
#	except Artista.DoesNotExist: # Artista no existe y se puede crear
#		artista = Artista(username = user, password = password, nombre = nombre,
#						  apellidos = apellidos, tipousuario = request.POST['tipoususario'],  correoe = request.GET['email'], pais = pais, direccion = direccion,
#						  codigopostal = codigopostal, telefono = telefono, ciudad = ciudad, activo = 1, 
#						  fechacreacion = datetime.datetime.now() + datetime.timedelta(hours = 2),
#						  fechaactivacion = datetime.datetime.now() + datetime.timedelta(hours = 2),
#						  ultimaaccionfecha = datetime.datetime.now() + datetime.timedelta(hours = 2),
#					      ultimoaccesofecha = datetime.datetime.now() + datetime.timedelta(hours = 2),
#					      ultimoaccesoip = get_client_ip(request), connect = 1, sesionactiva = 1)
#		artista.save()
#		dicc = {'content' : 'OK', 'mensaje' : {'username' : user}}
#	else: # el usuario ya existe
#		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Este artista ya existe'}}
#	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
#	return HttpResponse(data, 'application/json')

def borrar_artista(request,idartista, user):
	dicc = {}
	try:
		artista = Artista.objects.get(id = idartista, username = user)
		artista.delete()
		dicc = {'content' : 'OK'}

	except Artista.DoesNotExist: # Artista no existe y no puede ser borrado
		dicc = {'content' : 'KO', 'mensaje' :  'El artista %s no existe.' % user}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

# Tengo que hacer update_artista2
def update_artista(request, user, password, nombre, apellidos, tipousuario, pais, direccion, ciudad, codigopostal, telefono):
	dicc = {}
	try:
		artista = Artista.objects.get(username = user)
		artista.password = password
		artista.nombre = nombre
		artista.apellidos = apellidos
		artista.tipousuario = tipousuario
		artista.pais = pais
		artista.codigopostal = codigopostal
		artista.telefono = telefono
		artista.direccion = direccion
		artista.ciudad = ciudad
		artista.correoe = request.POST['email']

		artista.save()

		ar = {}
		ar = {'usuario' : artista.username, 'password' : artista.password, 'nombre' : artista.nombre,
		      'apellidos' : artista.apellidos, 'tipousuario' : artista.tipousuario, 'pais' : artista.pais,
		      'codigopostal' : artista.codigopostal, 'telefono' : artista.telefono, 
		      'direccion' : artista.direccion, 'ciudad' : artista.ciudad, 
		      'codartista' : artista.codartista, 'correoe' : artista.correoe}

		dicc = {'content' : 'OK', 'mensaje' : ar}

	except Artista.DoesNotExist:
		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Este artista NO existe'}}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def borrar_usuario(request, idartista, user):
	dicc = {}
	try:
		usuario = Artista.objects.get(id = idartista, username = user)
		usuario.delete()
		dicc = {'content' : 'OK'}
	except Usuario.DoesNotExist: # Usuario no existe y no puede ser borrado
		dicc = {'content' : 'KO', 'mensaje' :  'El usuario %s no existe.' % user}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

def update_usuario(request, user, password, nombre, apellidos, tipousuario, pais, direccion, ciudad, codigopostal, telefono):
	dicc = {}
	try:
		usuario = Artista.objects.get(username = user)
		usuario.password = password
		usuario.nombre = nombre
		usuario.apellidos = apellidos
		usuario.tipousuario = tipousuario
		usuario.pais = pais
		usuario.codigopostal = codigopostal
		usuario.telefono = telefono
		usuario.direccion = direccion
		usuario.ciudad = ciudad
		usuario.correoe = request.POST['email']

		usuario.save()

		ar = {}
		ar = {'usuario' : usuario.username, 'password' : usuario.password, 'nombre' : usuario.nombre,
		      'apellidos' : usuario.apellidos, 'tipousuario' : usuario.tipousuario, 'pais' : usuario.pais,
		      'codigopostal' : usuario.codigopostal, 'telefono' : usuario.telefono, 
		      'direccion' : usuario.direccion, 'ciudad' : usuario.ciudad, 
		      'codusuario' : usuario.codartista, 'correoe' : usuario.correoe}

		dicc = {'content' : 'OK', 'mensaje' : ar}

	except Artista.DoesNotExist:
		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Este artista NO existe'}}

	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')


#devuelve todos los datos del nuevo usuario si el usuario se ha creado con exito
@csrf_protect
def alta_usuario(request):
	dicc = {}
	try:
		usuario = Artista.objects.get(username = request.POST['user'], password = request.POST['password'])
	except Artista.DoesNotExist: # usuario no existe y se puede crear
		usuario = Artista(username = request.POST['user'], password = request.POST['password'], nombre = request.POST['nombre'],
						  apellidos = request.POST['apellidos'], tipousuario = request.POST['tipoususario'], 
						  correoe = request.POST['email'], pais = request.POST['pais'], 
						  direccion = request.POST['direccion'], codigopostal = request.POST['codigopostal'], 
						  telefono = request.POST['telefono'], ciudad = request.POST['ciudad'], activo = 1, 
						  fechacreacion = datetime.datetime.now() + datetime.timedelta(hours = 2),
						  fechaactivacion = datetime.datetime.now() + datetime.timedelta(hours = 2),
						  ultimaaccionfecha = datetime.datetime.now() + datetime.timedelta(hours = 2),
					      ultimoaccesofecha = datetime.datetime.now() + datetime.timedelta(hours = 2),
					      ultimoaccesoip = get_client_ip(request), connect = 1, sesionactiva = 1)
		usuario.save()
		dicc = {'content' : 'OK', 'mensaje' : {'username' : user}}
	else: # el usuario ya existe
		dicc = {'content' : 'KO', 'mensaje' : {'error' : 'Este usuario ya existe'}}
	data = '%s(%s);' % (request.GET.get('callback'), json.dumps(dicc))
	return HttpResponse(data, 'application/json')

# Funcion que devuelve la ip del cliente
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


