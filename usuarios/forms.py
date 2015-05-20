from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# esta clase deriva de UserCreationForm para que haga la gestion de los passwords
class CreacionUsuario(UserCreationForm):
	email = forms.EmailField() # email tiene que ser un email valido
	
	class Meta:
		model = User
		fields = ('username', 'email')

class AutenticacionEmail(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(label = 'Password', widget = forms.PasswordInput)

	def __init__(self, *args, **kwargs): # Constructor
		self.user_cache = None
		super(AutenticacionEmail, self).__init__(*args, **kwargs)

	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')

		# Intento autenticar el usuario con el metodo django authenticate
		self.user_cache = authenticate(email = email, password = password)

		if self.user_cache is None:
			raise forms.ValidationError('Usuario Incorrecto')
		elif not self.user_cache.is_active:
			raise forms.ValidationError('Usuario inactivo')

		return self.cleaned_data

	def get_user(self):
		return self.user_cache