from django.db import models
from django.contrib import admin

class Usuario(models.Model):
	username 			= models.CharField(max_length = 100)
	password 			= models.CharField(max_length = 100)
	connect  			= models.BooleanField(default = False)
	sesion				= models.CharField(max_length = 20, default="")
	ultimoaccesoip		= models.CharField(max_length = 32, default = "")
	ultimoaccesofecha 	= models.DateTimeField(default = None)
	sesionactiva		= models.BooleanField(default = False)

class Artista(models.Model):
	 nombre				= models.CharField(max_length = 100)
	 apellidos			= models.CharField(max_length = 200)
	 connect			= models.BooleanField(default = False)
	 username			= models.CharField(max_length = 32)
	 password 			= models.CharField(max_length = 100)
	 correoe		    = models.EmailField()
	 pais				= models.CharField(max_length = 200, default = "")
	 codigopostal		= models.CharField(max_length = 10, default = "")
	 telefono		    = models.CharField(max_length = 12)
	 fechacreacion	 	= models.DateTimeField()
	 activo				= models.BooleanField(default = False)
	 fechaactivacion	= models.DateTimeField()
	 ultimoaccesofecha  = models.DateTimeField(default = None)
	 ultimoaccesoip		= models.CharField(max_length = 32, default = "")
	 connect			= models.BooleanField(default = False)
	 estadosuscripcion	= models.IntegerField(default = -1)
	 direccion			= models.CharField(max_length = 250, default = "")
	 ciudad				= models.CharField(max_length = 250, default = "")
	 sesion 			= models.CharField(max_length = 20, default = "")
	 codartista			= models.CharField(max_length = 100)
	 ultimaaccionfecha	= models.DateTimeField(default = None)
	 sesionactiva		= models.BooleanField(default = False)

class Caricaturas(models.Model):
	idartista			= models.ForeignKey(Artista)
	titulo				= models.CharField(max_length = 200)
	tag					= models.CharField(max_length = 200)
	img_alta			= models.CharField(max_length = 500)
	img_miniatura		= models.CharField(max_length = 200)
	fecha_subida		= models.DateTimeField()
	facebook			= models.IntegerField(default = 0)
	twitter				= models.IntegerField(default = 0)
	googleplus			= models.IntegerField(default = 0)
	visualizaciones		= models.IntegerField(default = 0)

