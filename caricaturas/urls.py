# -*- encoding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from dibujos.crud import alta_usuario, alta_artista, alta_artista2, update_artista, update_usuario , borrar_artista, borrar_usuario
from dibujos.crud_caricaturas import borrar_caricatura, alta_caricatura, caricatura
from dibujos.views import  upload_file, import_uploader, start, prueba, subir_s3, login_usuario, login_usuario_crossdomain, login_artista, login_artista_crossdomain,  artistas, artista, administradores, usuarios_crossdomain, artistas_crossdomain, caricaturas_artista  #, ejemplo, sign_s3, 
from dibujos.crud import alta_usuario, alta_artista,  update_artista, update_usuario , borrar_artista, borrar_usuario #, alta_artista2,
from dibujos.crud_caricaturas import borrar_caricatura, alta_caricatura
from dibujos.views import  upload_file, import_uploader, start, prueba, subir_s3, login_usuario, login_usuario_crossdomain, login_artista, login_artista_crossdomain,  artistas, artista, usuarios_crossdomain, artistas_crossdomain, caricaturas_artista  #, ejemplo, sign_s3, 
from dibujos.crud_caricaturas import alta_caricatura, borrar_caricatura, update_caricatura
from django.conf.urls.static import static

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^prueba/', prueba),
    #url(r'^ejemplo/', ejemplo),
    #url(r'^sign_s3/', sign_s3),
    #url(r'^submit_form/', submit_form),
    url(r'^alta_usuario/$', alta_usuario, name = 'alta_usuario'),
    url(r'^login_usuario/(\w+)/(\S{5,})', login_usuario, name = 'login_usuario'),
    url(r'^login_usuario_crossdomain/(\w+)/(\S{5,})', login_usuario_crossdomain, name = 'login_usuario_crossdomain'),
    #url(r'^alta_artista/(\w+)/(\S{5,})/(\w+)/(\w+)/(\w+)(\w+)/(\w+)/(\w+)/(\w+)/', alta_artista2, name = 'alta_artista2'),
    url(r'^alta_artista/$', alta_artista, name = 'alta_artista'),
    url(r'^login_artista/(\w+)/(\S{5,})', login_artista, name = 'login_artista'),
    url(r'^login_artista_crossdomain/(\w+)/(\S{5,})', login_artista_crossdomain, name = 'login_artista_crossdomain'),
    url(r'^usuarios/$', artistas, name = 'usuarios'),
    url(r'^usuarios_crossdomain/$', usuarios_crossdomain, name = 'usuarios_crossdomain'),
    url(r'^artista/([0-9]+)/', artista, name = 'artista'),   
    url(r'^artistas/$', artistas, name = 'artistas'),
    url(r'^update_pass_usuario/$', update_pass_usuario, name = 'update_pass_usuario'),
    url(r'^administradores/$', administradores, name = 'administradores'),
    url(r'^artistas_crossdomain/$', artistas_crossdomain, name = 'artistas_crossdomain'),
    url(r'^update_artista/(\w+)/(\S{5,})/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/', update_artista, name = 'update_artista'),
    url(r'^update_usuario/(\w+)/(\w+)/(\S{5,})', update_usuario, name = 'update_usuario'),
    url(r'^borrar_artista/(\w+)/', borrar_artista, name = 'borrar_artista'),
    url(r'^borrar_usuario/(\w+)/', borrar_usuario, name = 'borrar_usuario'),
    url(r'^alta_caricatura/([0-9]+)/(\w+)/(\w+)/(\w+)/(\w+)/', alta_caricatura, name = 'alta_caricatura'),
    url(r'^caricatura/([0-9]+)/', caricatura, name = 'caricatura'),
    url(r'^borrar_caricatura/(\w+)/(\w+)/', borrar_caricatura, name = 'borrar_caricatura'),
    url(r'^update_caricatura/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/', update_caricatura, name = 'update_caricatura'),
    #url(r'^subir_imagen/', subir_imagen),
    #url(r'^subir_caricatura/', subir_caricatura),
    url(r'^subir_s3/', subir_s3, name = 'subir_s3'),
    url(r'^alta_caricatura/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/', alta_caricatura, name = "alta_caricatura"),
    url(r'^borrar_caricatura/(\w+)/(\w+)/', borrar_caricatura, name = 'borrar_caricatura'),
    url(r'^caricaturas_artista/([0-9]+)/', caricaturas_artista, name = 'caricaturas_artista'),
    #---------------------------------
    url(r'start$', start, name = "start"),
    url(r'ajax-upload$', upload_file, name = "my_ajax_upload"),
    #---------------------------------------
    #url(r'^signup/(\w+)/(password)', signup, name = 'signup'),
    #url(r'^signin/', signin, name = 'signin'),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)