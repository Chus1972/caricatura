from django.contrib import admin
from .models import *

#class UsuarioAdmin(admin.ModelAdmin):
#	list_display = ('username', 'password',  'sesion', 'ultimoaccesoip', 'ultimoaccesofecha', 'connect', 'sesionactiva',)


#class ClienteAdmin(admin.ModelAdmin):
#	list_display = ('username', 'password', )

#admin.site.register(Usuario, UsuarioAdmin)
#admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Usuario)
admin.site.register(Artista)
admin.site.register(caricaturas)
# Register your models here.
