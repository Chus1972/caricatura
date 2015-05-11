from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
import os, base64, hmac, urllib
from django.template.context_processors import csrf


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
	print AWS_ACCESS_KEY
	print AWS_SECRET_KEY
	print S3_BUCKET

	print 'nombre ficher : %s' % file_name

	object_name = urllib.quote_plus(request.args.get('file_name'))
	print 'object_name: ' 
	print object_name
	mime_type = request.args.get('file_type')
	print 'mime_type'
	print mime_type
	expires = long(time.time()+60*60*24)
	amz_headers = "x-amz-acl:public-read"

	put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)
	print 'put_request'
	print put_request

	#signature = base64.encodestring(hmac.new(AWS_SECRET_KEY, put_request, sha1).digest())
	signature = base64.encodestring(hmac.new(AWS_SECRET_KEY, put_request.encode('utf8'), sha1).digest())

	signature = urllib.quote_plus(signature.strip())
	print 'signature'
	print signature

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

	username = request.GET.get("username")
	full_name = request.GET.get("full_name")
	avatar_url = request.GET.get("avatar_url")


	print username
	print full_name
	print avatar_url

	return render_to_response("prueba.html", c)
	