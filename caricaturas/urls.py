from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from dibujos.views import prueba, subir_s3, alta_usuario, login_usuario, login_artista, alta_artista #, ejemplo, sign_s3, 
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
    url(r'^alta_artista/(\w+)/(\S{5,})/(\w+)/(\w+)/(\w+)/(\w+)(\w+)/(\w+)/(\w+)/(\w+)/', alta_artista, name = 'alta_artista'),
    url(r'^login_artista/(\w+)/(\S{5,})', login_artista, name = 'login_artista'),
    url(r'^subir_caricatura/', subir_s3),
    url(r'^subir_s3/', subir_s3, name = 'subir_s3'),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)