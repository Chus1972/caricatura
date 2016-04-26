from django.shortcuts import render
from .forms import CreacionUsuario, AutenticacionEmail
from django.contrib.auth import login
from dibujos.models import Usuario

def signup(request):
	form = CreacionUsuario(request.GET or None) # El formulario se crea con los datos. Si no hay nada esta vacio

	if form.is_valid(): # Esto valida que todo este correcto
		form.save() # Esto crea el usuario. Toma los datos y crea un usuario

		#guardaUsuarioBDD(request)

		# Aqui tambien se debe loguer al usuario
		# crear usuario aqui en la tabla usuarios

	return render(request, 'signup.html', {'form' : form})

def signin(request):

	form = AutenticacionEmail(request.GET or None)
	print 'entra en signin con form : %s' % form.is_valid() 
	if form.is_valid(): # Se valida que exista
		print 'entra en if de signin'
		login(request, form.get_user())

		# Esta logueado,entonces redirecciono a donde se sube la caricatura
		return render(request, 'subir_caricatura.html', {'form' : form})

	return render(request, 'signin.html', {'form' : form})

def guardaUsuarioBDD(request):
	nombre = request.GET['username']
	pas = request.GET['password']

	usuario = Usuario(username = nombre,
					  password = pas,
					  connect = True,
					  sesion = 'activa',
					  ultimoaccesoip = '123.456.789.012',
					  ultimoaccesofecha = datetime.datetime.now(),
					  sesionactiva = 'si')
	usuario.save()

