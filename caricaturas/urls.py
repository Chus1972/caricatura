from django.conf.urls import include, url
from django.contrib import admin
from dibujos.views import prueba, ejemplo, sign_s3, submit_form

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'caricaturas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^prueba/', prueba),
    url(r'^ejemplo/', ejemplo),
    url(r'^sign_s3/', sign_s3),
    url(r'^submit_form/', submit_form),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
)