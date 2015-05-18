from django.db import models

class Usuario(models.Model):
	username 			= models.CharField(max_length = 100)
	password 			= models.CharField(max_length = 20)
	connect  			= models.BooleanField
	sesion				= models.CharField(max_length = 20)
	ultimoaccesoip		= models.CharField(max_length = 32)
	ultimoaccesofecha 	= models.DateTimeField
	sesionactiva		= models.BooleanField

class Cliente(models.Model):
	 nombre				= models.CharField(max_length = 100)
	 apellidos			= models.CharField(max_length = 200)
	 connect			= models.BooleanField
	 username			= models.CharField(max_length = 32)
	 password 			= models.CharField(max_length = 100)
	 correoe		    = models.EmailField
	 pais				= models.CharField(max_length = 200)
	 codigopostal		= models.CharField(max_length = 10)
	 telefono		    = models.CharField(max_length = 12)
	 fechacreacion	 	= models.DateTimeField
	 activo				= models.BooleanField
	 fechaactivacion	= models.DateTimeField
	 ultimoaccesofecha  = models.DateTimeField
	 ultimoaccesoip		= models.CharField(max_length = 32)
	 connect			= models.BooleanField
	 estadosuscripcion	= models.IntegerField
	 direccion			= models.CharField(max_length = 250)
	 ciudad				= models.CharField(max_length = 250)
	 sesion 			= models.CharField(max_length = 20)
	 codcliente			= models.CharField(max_length = 100)
	 ultimaaccionfecha	= models.DateTimeField
	 sesionactiva		= models.BooleanField
