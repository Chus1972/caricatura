from django.conf.urls import include, url
from django.contrib import admin
from dibujos.views import prueba

urlpatterns = [
    # Examples:
    # url(r'^$', 'caricaturas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^prueba/', prueba),
]
