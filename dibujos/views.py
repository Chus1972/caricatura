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
	AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
	AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
	S3_BUCKET = os.environ.get('S3_BUCKET')

	object_name = request.args.get('s3_object_name')
	mime_type = request.args.get('s3_object_type')
	expires = long(time.time()+10)
	amz_headers = "x-amz-acl:public-read"

	put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)

	signature = base64.encodestring(hmac.new(AWS_SECRET_KEY, put_request, sha1).digest())

	signature = urllib.quote_plus(signature.strip())

	url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)

	return json.dumps({
		'signed_request' : '%s?AWSAccessKeyId=%s&Expires=%d&Signature=%s' % (url, AWS_SECRET_KEY, expires, signature),
		'url' : url
		})

def submit_form(request):
	c = {}
	c.update(csrf(request))

	username = request.form["username"]
	full_name = request.form["full_name"]
	avatar_url = request.form["avatar_url"]
	update_account(username, full_name, avatar_url)

	return render_to_response("prueba.html", c)
	