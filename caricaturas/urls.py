# -*- encoding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from dibujos.crud import alta_usuario, alta_artista, update_artista, update_usuario , borrar_artista, borrar_usuario
from dibujos.views import prueba_ejemplo, prueba, subir_s3, login_usuario, login_artista, usuarios, artistas, usuarioss  #, ejemplo, sign_s3, 
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
    url(r'^prueba_ejemplo/', prueba_ejemplo),
    url(r'^alta_usuario/(\w+)/(\S{5,})', alta_usuario, name = 'alta_usuario'),
    url(r'^login_usuario/(\w+)/(\S{5,})', login_usuario, name = 'login_usuario'),
    url(r'^alta_artista/(\w+)/(\S{5,})/(\w+)/(\w+)/(\w+)/(\w+)(\w+)/(\w+)/(\w+)/(\w+)/', alta_artista, name = 'alta_artista'),
    url(r'^login_artista/(\w+)/(\S{5,})', login_artista, name = 'login_artista'),
    url(r'^usuarios/$', usuarios, name = 'usuarios'),
    url(r'^usuarioss/$', usuarioss, name = 'usuarioss'),
    url(r'^artistas/$', artistas, name = 'artistas'),
    url(r'^update_artista/(\w+)/(\w+)/(\S{5,})/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/', update_artista, name = 'update_artista'),
    url(r'^update_usuario/(\w+)/(\w+)/(\S{5,})', update_usuario, name = 'update_usuario'),
    url(r'^borrar_artista/(\w+)/', borrar_artista, name = 'borrar_artista'),
    url(r'^borrar_usuario/(\w+)/', borrar_usuario, name = 'borrar_usuario'),
    url(r'^subir_caricatura/', subir_s3),
    url(r'^subir_s3/', subir_s3, name = 'subir_s3'),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)