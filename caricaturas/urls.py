# -*- encoding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from dibujos.crud import alta_usuario, alta_artista, update_artista, update_usuario , borrar_artista, borrar_usuario
from dibujos.crud_caricaturas import borrar_caricatura, alta_caricatura
from dibujos.views import  prueba, subir_s3, subir_imagen, login_usuario, login_usuario_crossdomain, login_artista, login_artista_crossdomain, usuarios, artistas, usuarios_crossdomain, artistas_crossdomain  #, ejemplo, sign_s3, 
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'caricaturas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^prueba/', prueba),
    #url(r'^ejemplo/', ejemplo),
    #url(r'^sign_s3/', sign_s3),
    #url(r'^submit_form/', submit_form),
    url(r'^alta_usuario/(\w+)/(\S{5,})', alta_usuario, name = 'alta_usuario'),
    url(r'^login_usuario/(\w+)/(\S{5,})', login_usuario, name = 'login_usuario'),
    url(r'^login_usuario_crossdomain/(\w+)/(\S{5,})', login_usuario_crossdomain, name = 'login_usuario_crossdomain'),
    url(r'^alta_artista/(\w+)/(\S{5,})/(\w+)/(\w+)/(\w+)/(\w+)(\w+)/(\w+)/(\w+)/(\w+)/', alta_artista, name = 'alta_artista'),
    url(r'^login_artista/(\w+)/(\S{5,})', login_artista, name = 'login_artista'),
    url(r'^login_artista_crossdomain/(\w+)/(\S{5,})', login_artista_crossdomain, name = 'login_artista_crossdomain'),
    url(r'^usuarios/$', usuarios, name = 'usuarios'),
    url(r'^usuarios_crossdomain/$', usuarios_crossdomain, name = 'usuarios_crossdomain'),
    url(r'^artistas/$', artistas, name = 'artistas'),
    url(r'^artistas_crossdomain/$', artistas_crossdomain, name = 'artistas_crossdomain'),
    url(r'^update_artista/(\w+)/(\w+)/(\S{5,})/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/', update_artista, name = 'update_artista'),
    url(r'^update_usuario/(\w+)/(\w+)/(\S{5,})', update_usuario, name = 'update_usuario'),
    url(r'^borrar_artista/(\w+)/', borrar_artista, name = 'borrar_artista'),
    url(r'^borrar_usuario/(\w+)/', borrar_usuario, name = 'borrar_usuario'),
    url(r'^subir_imagen/', subir_imagen),
    url(r'^subir_s3/(\w+)/', subir_s3, name = 'subir_s3'),
    url(r'^alta_caricatura/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/', alta_caricatura, name = "alta_caricatura"),
    url(r'^borrar_caricatura/(\w+)/(\w+)/', borrar_caricatura, name = 'borrar_caricatura'),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)