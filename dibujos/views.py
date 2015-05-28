from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json,os
from dibujos.models import *
#import sys,os, base64, hmac, urllib, hashlib
from django.template.context_processors import csrf
import time, datetime
from django.template import RequestContext
#from django.contrib.auth.models import User
import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.core.exceptions import ObjectDoesNotExist

def prueba(request):
 	data = {'hola' : 'adios'}

 	return HttpResponse(json.dumps(data), "application/json")

def prueba_ejemplo(request):
	return render(request, 'ejemplo_prueba.html')

def login_usuario(request, user, password):
	dicc = {}
	try:
		usuario = Usuario.objects.get(username = user, password = password)
		dicc = {'content' : 'OK', 'mensaje' : { 'usuario' : usuario.username, 'conectado' : usuario.connect, 
		        'sesion' : usuario.sesion, 'ultimoaccesoip' : usuario.ultimoaccesoip,
		        'ultimoaccesofecha' : usuario.ultimoaccesofecha.isoformat(), 
		        'sesionactiva' : usuario.sesionactiva}}

	except Usuario.DoesNotExist:
		dicc = {'content' : 'KO'}
	
	return HttpResponse('callback(' + json.dumps(dicc), 'application/json') + ')'


def login_artista(request, user, password):
	dicc = {}
	try:
		artista = Artista.objects.get(username = user, password = password)
		dicc = {'content' : 'OK', 'mensaje' : {'nombre' : artista.nombre, 'apellidos' : artista.apellidos,
			    'username' : artista.username, 'pais' : artista.pais, 
		        'codigopostal' : artista.codigopostal, 'telefono' : artista.telefono,
		        'direccion' : artista.direccion, 'ciudad' : artista.ciudad, 
		        'sesion' : artista.sesion, 'codartista' : artista.codartista,
		        'connect' : artista.connect, 'ultimoaccesoip' : artista.ultimoaccesoip,
		        'ultimoaccesofecha' : artista.ultimoaccesofecha.isoformat(),
		        'estadosuscripcion' : artista.estadosuscripcion,
		        'sesionactiva' : artista.sesionactiva, 'activo' : artista.activo}}
	except Artista.DoesNotExist, e:
		dicc = {'content' : 'KO'}
	return HttpResponse(json.dumps(dicc), 'application/json')

def usuarios(request):
	dicc = {}
	listaUsuarios = []
	try:
		usuarios = Usuario.objects.all()
		for usuario in usuarios:
			listaUsuarios.append({'username' : usuario.username, 'sesion' : usuario.sesion, 'conectado' : usuario.connect, 
							      'ultimo acceso ip' : usuario.ultimoaccesoip, 'ultimo acceso fecha' : usuario.ultimoaccesofecha.isoformat(),
							      'sesion activa' : usuario.sesionactiva})

		#if request.GET['callback']:
		#	respuesta = "%s(%s)" % (request.GET['callback'],{'content' : 'OK', 'mensaje' : listaUsuarios})
		dicc = 'callback(%s)' % {'content' : 'OK', 'mensaje' : listaUsuarios}
		#dicc = {'content' : 'OK', 'mensaje' : listaUsuarios}
	except Exception as e:
		#dicc = 'callback(%s)' % {'content' : 'KO', 'error' : e}
		dicc = {'content' : 'KO', 'error' : e}

	#if request.method == 'OPTIONS':
	#	respuesta = HttpResponse(json.dumps(dicc), 'application/json')
	#	respuesta["Access-Control-Allow-Origin"] = '*'
	#	respuesta["Access-Control-Allow-Methods"] = 'GET, OPTIONS, POST, '
	#	respuesta["Access-Control-Allow-Headers"] = "X-Requested-With"
	respuesta = HttpResponse(json.dumps(dicc), 'application/json')
	return respuesta

def usuarioss(request):
	print 'entra a usuarioss'
	dicc = {}
	listaUsuarios = []
	try:
		usuarios = Usuario.objects.all()
		for usuario in usuarios:
			listaUsuarios.append({'username' : usuario.username, 'sesion' : usuario.sesion, 'conectado' : usuario.connect, 
							      'ultimo acceso ip' : usuario.ultimoaccesoip, 'ultimo acceso fecha' : usuario.ultimoaccesofecha.isoformat(),
							      'sesion activa' : usuario.sesionactiva})
		print 'sale for'
		#if request.GET['callback']:
		#	respuesta = "%s(%s)" % (request.GET['callback'],{'content' : 'OK', 'mensaje' : listaUsuarios})
		#dicc = 'callback(%s)' % {'content' : 'OK', 'mensaje' : listaUsuarios}
		dicc = {'content' : 'OK', 'mensaje' : listaUsuarios}
	except Exception as e:
		print 'pasa exepcion'
		#dicc = 'callback(%s)' % {'content' : 'KO', 'error' : e}
		dicc = {'content' : 'KO', 'error' : e}

	if request.method == 'OPTIONS':
		print 'entra'
		respuesta = HttpResponse(json.dumps(dicc), 'application/json')
		respuesta["Access-Control-Allow-Origin"] = '*'
		respuesta["Access-Control-Allow-Methods"] = 'GET, OPTIONS, POST'
		respuesta["Access-Control-Allow-Headers"] = "X-Requested-With"
	return respuesta

def artistas(request):
	dicc = {}
	listaArtistas = []
	try:
		artistas = Artista.objects.all()
		for artista in artistas:
			listaArtistas.append({'nombre' : artista.nombre, 'apellidos' : artista.apellidos, 'username' : artista.username, 
							      'pais' : artista.pais, 'codigo postal' : artista.codigopostal, 'telefono' : artista.telefono,  
							      'telefono' : artista.telefono, 'direccion' : artista.direccion, 'ciudad' : artista.ciudad, 
							      'sesion' : artista.sesion, 'codigo artista' : artista.codartista,  'conectado' : artista.connect, 
							      'ultimo acceso ip' : artista.ultimoaccesoip, 'ultimo acceso fecha' : artista.ultimoaccesofecha.isoformat(),
							      'estado suscripcion' : artista.estadosuscripcion, 'sesion activa' : artista.sesionactiva,
							      'activo' : artista.activo, 'correo electronico' : artista.correoe, 'ultima accion fecha' : artista.ultimaaccionfecha.isoformat(),
							      'fecha creacion' : artista.fechacreacion.isoformat(), 'fecha activacion' : artista.fechaactivacion.isoformat()})
		dicc = {'content' : 'OK', 'mensaje' : listaArtistas}
	except Exception as e:
		dicc = {'content' : 'KO', 'error' : e}

	return HttpResponse(json.dumps(dicc), 'application/json')


def subir_s3(request):
	print 'Entra subir_s3: %s' % request.POST
	if request.POST: # Esto quiere decir que se han llenado los datos del formulario
		nombre_fichero = request.POST['file_input']
		print 'entra en if : %s' % nombre_fichero

		# Hace la subida del fichero a s3
		con_s3 = boto.connect_s3()
		# Creamos un bucket con el nombre del artista
		# Si el bucket ya existe 
		# Se recoge los datos de la base de datos
		nombre_bucket = "nuevo_bucket"

		bucket = con_s3.create_bucket(nombre_bucket)
		k = Key(bucket)
		k.key = 'nombreArtista' + nombre_fichero # Nombre con que sera guardado el fichero
		k.set_contents_from_filename(nombre_fichero) # Nombre del fichero a subir

	return render(request, 'signup.html')


# Funcion que devuelve la ip del cliente
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



# def ejemplo(request):
# 	return render(request, 'ejemplo.html', context_instance=RequestContext(request))

# def sign(key, msg):
# 	return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

# def get_signature_key(key, dateStamp, regionName, serviceName):
# 	kDate = sign(("AWS4" + key).encode("utf-8"), dateStamp)
# 	kRegion = sign(kDate, regionName)
# 	kService = sign(kRegion, serviceName)
# 	kSigning = sign(kService, "aws4_request")
# 	return kSigning

# def sign_s3(request):
#         # esto no chuta
# 	print 'entra en sign_s3'
# 	method = 'GET'
# 	service = 's3'
# 	host = 'imagenesprueba.s3.amazonaws.com'
# 	region = 'eu-central-1'
# 	endpoint = 'imagenesprueba.s3-website.eu-central-1.amazonaws.com'
# 	print '11111111111111111'
# 	AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
#  	AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
#  	S3_BUCKET = os.environ.get('S3_BUCKET')
#  	print '22222222222222222'

#  	t = datetime.datetime.utcnow()
#  	amzdate = t.strftime('%Y%m%dT%H%M%SZ')
#  	datestamp = t.strftime('%Y%m%d')
#  	print '333333333333333333'

#  	#-------------------------------------------------
#  	# PASO 1 : Creacion de request canonico
#  	#-------------------------------------------------

#  	canonical_uri = '/imagenesprueba/'

#  	canonical_headers = 'host:' + host + '\n'
#  	print 'canonical_headers : %s' % canonical_headers
#  	signed_headers = 'host'

#  	algoritmo = 'AWS4-HMAC-SHA256'
#  	credencial_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'
#  	print 'credencial_scope : %s' % credencial_scope
#  	canonical_querystring = 'Action=s3:PutObject&Version=2012-10-17'
#  	canonical_querystring +=  '&X-Amz-Algorithm=' + algoritmo
#  	print canonical_querystring +' 1'
#  	canonical_querystring += '&X-Amz-Credential=' + urllib.quote_plus(AWS_ACCESS_KEY + '/' + credencial_scope)
#  	print canonical_querystring + ' 2 '
#  	canonical_querystring += '&X-Amz-Date=' + amzdate
#  	print canonical_querystring + ' 3'
#  	canonical_querystring += '&X-Amz-Expires=100'
#  	print canonical_querystring + ' 4'
#  	canonical_querystring += '&X-Amz-SignedHeaders=' + signed_headers
#  	print 'canonical_querystring : %s' % canonical_querystring
 	
#  	payload_hash = hashlib.sha256('').hexdigest()
#  	print 'payload_hash %s' % payload_hash

#  	canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash
#  	print 'canonical_request %s' % canonical_request
# 	#-------------------------------------------------
#  	# PASO  2: Creacion del string de la firma
#  	#-------------------------------------------------
#  	string_to_sign = algoritmo + '\n' + amzdate + '\n' + credencial_scope + '\n' + hashlib.sha256(canonical_request).hexdigest()
#  	print 'string_to_sign : %s' % string_to_sign
#  	#-------------------------------------------------
#  	# PASO 3 : Calculo de la firma
#  	#-------------------------------------------------
#  	signing_key = get_signature_key(AWS_SECRET_KEY, datestamp, region, service)
#  	print 'signing_key : %s' % signing_key
#  	signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
#  	print 'signature : %s' % signature
#  	#-------------------------------------------------
#  	# PASO 4 : Anade la firma al request
#  	#-------------------------------------------------
#  	canonical_querystring += '&X-Amz-Signarure=' + signature
#  	print 'canonical_querystring2 : %s' % canonical_querystring
#  	#-------------------------------------------------
#  	# PASO 5 : Envio del request
#  	#-------------------------------------------------
#  	request_url = endpoint + '?' + canonical_querystring
#  	print 'request_url : %s' % request_url

#  	return HttpResponse(json.dumps({'url' : request_url, 'signed_request' : signature}))

# def sign_s3(request):
# 	print 'Entra en sign_s3'
# 	AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
# 	AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
# 	S3_BUCKET = os.environ.get('S3_BUCKET')

# 	method = 'GET'
# 	service = 's3'
# 	host = 's3.amazonaws.com'
# 	region = 'eu-central-1'
# 	#endpoint = 'https://%s.%s-website.%s.amazonaws.com' % (S3_BUCKET, service, region)
# 	endpoint = 'https://%s.amazonaws.com' % service

# 	print 'endpoint : %s' % endpoint


# 	object_name = request.GET['file_name']
# 	print 'object_name: %s' % object_name

	

# 	#creo una fecha para la cabecera y el string de las credenciales
# 	t = datetime.datetime.utcnow()
# 	amzdate = t.strftime('%Y%m%dT%H%M%SZ')
# 	print 'amzdate : %s' % amzdate
# 	datestamp = t.strftime('%Y%m%d')
# 	print 'datestamp : %s' % datestamp
#  	#------------------------------------------------------------------------------------------------
# 	# Creo la respuesta canonica - PASO 1
# 	canonical_uri = object_name
# 	canonical_query_string = ""
# 	canonical_headers = 'host:%s\nx-amz-date:%s\n' % (host, amzdate)
# 	print 'canonical_header : %s ' % (canonical_headers)
# 	signed_headers = 'host;x-amz-date'
# 	print "signed_headers: %s" % signed_headers
# 	payload_hash = hashlib.sha256("").hexdigest()
# 	print payload_hash
# 	print 'payload_hash : %s' % payload_hash

# 	mime_type = request.GET['file_type']

# 	# Canonical Request
# 	canonical_request = "%s\n%s\n%s\n%s\n%s\n%s" % (method, canonical_uri, canonical_query_string, canonical_headers, signed_headers, payload_hash) 
# 	print 'canonical_request : %s ' % canonical_request
#  	#------------------------------------------------------------------------------------------------
# 	# String para firmar - PASO 2
# 	#------------------------------------------------------------------------------------------------
	
# 	algoritmo = 'AWS4-HMAC-SHA256'
# 	credencial_scope = "%s/%s/%s/aws4_request" % (datestamp, region, service)
# 	print 'credencial_scope : %s' % (credencial_scope)
# 	string_para_firmar = "%s\n%s\n%s\n%s" % (algoritmo, amzdate, credencial_scope, hashlib.sha256(canonical_request).hexdigest())
# 	print 'string para firmar : %s' % (string_para_firmar)
# 	#------------------------------------------------------------------------------------------------
# 	# Calcula la firma - PASO 3
# 	#------------------------------------------------------------------------------------------------
# 	signing_key = get_signature_key(AWS_SECRET_KEY, datestamp, region, service)
# 	firma = hmac.new(signing_key, (string_para_firmar).encode('utf-8'), hashlib.sha256).hexdigest()
# 	print 'firma : %s' % (firma)
# 	#------------------------------------------------------------------------------------------------
# 	# Anade la informacion firmada al request - PASO 4
# 	#------------------------------------------------------------------------------------------------
# 	autorizacion_header = "%s Credential=%s/%s, SignedHeaders=%s, Signature=%s" % (algoritmo, AWS_ACCESS_KEY, credencial_scope, signed_headers, firma)
# 	headers = {'x-amz-date':amzdate, 'Authorization':autorizacion_header}

# 	#------------------------------------------------------------------------------------------------
# 	# Envio el request
# 	request_url = "%s?%s" % (endpoint, canonical_query_string)
# 	print 'request_url: %s' % request_url
	
# 	print 'json.dumps : '
# 	print HttpResponse(json.dumps({
# 		'signed_request' : firma,
# 		'url' : request_url,
# 		}))

# 	return HttpResponse(json.dumps({
# 		'signed_request' : firma,
# 		'url' : request_url,
# 		}), 'application/json')

# def submit_form(request):
# 	print 'ENTRA SUBMIT_FORM'
# 	c = {}
# 	c.update(csrf(request))
# 	print 'Esto es c.update : '
# 	print c

# 	username = request.POST["username"]
# 	full_name = request.POST["full_name"]
# 	avatar_url = request.POST["avatar_url"]

# 	print 'username : %s' % username
# 	print 'full_name : %s' % full_name
# 	print 'avatar_url : %s' % avatar_url

# 	return render_to_response("prueba.html", c, context_instance=RequestContext(request))
	
