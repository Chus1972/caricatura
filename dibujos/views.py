from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
import os, base64, hmac, urllib
from django.template.context_processors import csrf
import time
from hashlib import sha256
import datetime


def prueba(request):
	data = {'hola' : 'adios'}

	return HttpResponse(json.dumps(data), "application/json")
# Create your views here

def ejemplo(request):
	return render(request, 'ejemplo.html')

def sign(key, msg):
	return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def get_signature_key(key, dateStamp, regionName, serviceName):
	kDate = sign(("AWS4" + key).encode("utf-8"), dateStamp)
	kRegion = sign(kDate, regionName)
	kService = sign(kRegion, serviceName)
	kSigning = sign(kService, "aws4_request")
	return kSigning

def sign_s3(request):
	print 'Entra en sign_s3'
	AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
	AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
	S3_BUCKET = os.environ.get('S3_BUCKET')

	object_name = request.GET['file_name']
	print 'object_name: %s' % object_name

	method = 'PUT'
	service = 's3'
	host = 's3.amazonaws.com'
	region = 'eu-central-1'
	endpoint = 'https://%s.%s-website.%s.amazonaws.com' % (S3_BUCKET, service)
	print "endpoint : %s" % (endpoint)

	#creo una fecha para la cabecera y el string de las credenciales
	t = datetime.datetime.utcnow()
	amzdate = t.strftime('%Y%m%dT%H%M%SZ')
	datestamp = t.strftime('%Y%m%d')
	print 'datestamp : %s' % (datestamp)
 	#------------------------------------------------------------------------------------------------
	# Creo la respuesta canonica - PASO 1
	canonical_uri = object_name
	canonical_query_string = ""
	canonical_headers = 'host:%s\nx-amz-date:%s\n' % (host, amzdate)
	print 'canonical_header : %s ' % (canonical_headers)
	signed_headers = 'host;x-amz-date'
	payload_hash = hashlib.sha256('').hexdigest()

	mime_type = request.GET['file_type']

	# Canonical Request
	canonical_request = "%s\n%s\n%s\n%s\n%s\n%s" % (method, canonical_uri, canonical_query_string, canonical_headers, signed_headers, payload_hash) 
	print 'canonical_request %s ' % (canonical_request)
 	#------------------------------------------------------------------------------------------------
	# String para firmar - PASO 2
	#------------------------------------------------------------------------------------------------
	
	algoritmo = 'AWS-HMAC-SHA256'
	credencial_scope = "%s/%s/%s/aws4_request" % (datestamp, region, service)
	print 'credencial_scope : %s' % (credencial_scope)
	string_para_firmar = "%s\n%s\n%s\n%s" % (algoritmo, amzdate, credencial_scope, hashlib.sha256(canonical_request).hexdigest())
	print 'string para firmar : %s' % (string_para_firmar)
	#------------------------------------------------------------------------------------------------
	# Calcula la firma - PASO 3
	#------------------------------------------------------------------------------------------------
	signing_key = get_signature_key(AWS_SECRET_KEY, datestamp, region, service)
	firma = hmac.new(signing_key, (string_para_firmar).encode('utf-8'), hashlib.sha256).hexdigest()
	print 'firma : %s' % (firma)
	#------------------------------------------------------------------------------------------------
	# Anade la informacion firmada al request - PASO 4
	#------------------------------------------------------------------------------------------------
	autorizacion_header = "%s Credential=%s/%s, SignedHeaders=%s, Signature=%s" % (algoritmo, AWS_ACCESS_KEY, credencial_scope, signed_headers, firma)
	headers = {'x-amz-date':amzdate, 'Authorization':autorizacion_header}

	#------------------------------------------------------------------------------------------------
	# Envio el request
	request_url = "%s?%s" % (endpoint, canonical_query_string)
	
	
	print 'json.dumps : '
	print HttpResponse(json.dumps({
		'signed_request' : request_url,
		'url' : url,
		}))

	return HttpResponse(json.dumps({
		'signed_request' : request_url,
		'url' : url,
		}), 'application/json')

def submit_form(request):
	print 'ENTRA SUBMIT_FORM'
	c = {}
	c.update(csrf(request))
	print 'Esto es c.update : '
	print c

	username = request.POST["username"]
	full_name = request.POST["full_name"]
	avatar_url = request.POST["avatar_url"]

	print 'username : %s' % username
	print 'full_name : %s' % full_name
	print 'avatar_url : %s' % avatar_url

	return render_to_response("prueba.html", c)
	