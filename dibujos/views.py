from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
import os, base64, hmac, urllib
from django.template.context_processors import csrf
import time
from hashlib import sha1


def prueba(request):
	data = {'hola' : 'adios'}

	return HttpResponse(json.dumps(data), "application/json")
# Create your views here

def ejemplo(request):
	return render(request, 'ejemplo.html')

def sign_s3(request):
	print 'Entra en sign_s3'
	AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
	AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
	S3_BUCKET = os.environ.get('S3_BUCKET')
	print '------r------'
	print AWS_ACCESS_KEY
	print AWS_SECRET_KEY
	print S3_BUCKET
	print '------w------'
	print request
	print 'nombre ficher : %s' % request.GET['file_name']

	#object_name = urllib.quote_plus(request.GET('file_name'))
	object_name = request.GET['file_name']
	print 'object_name: ' 
	print object_name
	mime_type = request.GET['file_type']
	print 'mime_type'
	print mime_type
	try:
		expires = long(time.time()+60*60*24)
	except Exception, e:
		print 'excepcion en try '
		print e
	print 'expires'
	print expires
	amz_headers = "x-amz-acl:public-read"
	print 'amz_headers'
	print amz_headers

	put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)
	print 'put_request'
	print put_request

	print 'signature ?? '
	#signature = base64.encodestring(hmac.new(AWS_SECRET_KEY, put_request, sha1).digest())
	try:
		print 'entra en try - '
		signature = base64.encodestring(hmac.new(AWS_SECRET_KEY, put_request.encode('utf8'), sha1).digest())
		print signature
	except Exception, e:
		print 'excepcion en try 2 '
		print e

	#try:
	#	signature = urllib.quote_plus(signature.strip())
	#except Exception, e:
	#	print 'excepcion en signature :' 
	#	print e
	print 'S3_BUCKET : %s ' % S3_BUCKET

	url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)
	print 'url'
	print url
	
	print 'json.dumps : '
	print json.dumps({
		'signed_request' : '%s?AWSAccessKeyId=%s&Expires=%s&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature),
		'url' : url
		})

	return json.dumps({
		'signed_request' : '%s?AWSAccessKeyId=%s&Expires=%s&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature),
		'url' : url
		})

def submit_form(request):
	print 'ENTRA SUBMIT_FORM'
	c = {}
	c.update(csrf(request))
	print 'Esto es c.update : '
	print c

	username = request.GET["username"]
	full_name = request.GET["full_name"]
	avatar_url = request.GET["avatar_url"]

	print 'username : %s' % username
	print 'full_name : %s' % full_name
	print 'avatar_url : %s' % avatar_url

	return render_to_response("prueba.html", c)
	