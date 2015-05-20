from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from dibujos.views import prueba, subir_s3 #, ejemplo, sign_s3, 
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
    url(r'^signup/', 'usuarios.views.signup', name = 'signup'),
    url(r'^signin/', 'usuarios.views.signin', name = 'signin'),
    url(r'^subir_caricatura/', subir_s3),
    url(r'^subir_s3/', 'dibujos.views.subir_s3', name = 'subir_s3'),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)