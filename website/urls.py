from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^login/?$', views.Login.as_view(), name='login'),
    url(r'^pelicula/(?P<pk>\d+)/?$', views.DetallePelicula.as_view(), name='pelicula'),
    url(r'^nuestros-cines/?$', views.ListadoCine.as_view(), name='cine'),
    url(r'^$', views.Home.as_view(), name='home'),
]
