from django.shortcuts import render
from django.http import HttpResponse
import json

def prueba(request):
	data = {'hola' : 'adios'}

	return HttpResponse(json.dumps(data), "application/json")
# Create your views here.
