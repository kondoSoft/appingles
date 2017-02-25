from django.conf.urls import patterns, include, url
from calificaciones import views

from django.contrib import admin
admin.autodiscover()
from calificaciones.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appingles.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', views.buscar_matricula),

    url(r'^clasifica/(?P<matricula>\d+)&(?P<clasificacion>\w+)/', views.buscar_clasificacion),

    url(r'^archivo/$', views.importar_archivo),

    url(r'^login/$', 'django.contrib.auth.views.login', name = 'login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name = 'logout'),
)
