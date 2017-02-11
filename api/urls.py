from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^cartelera/(?P<cine>\d+)/(?P<pelicula>\d+)/(?P<fecha>\d{4}-\d{2}-\d{2})/?$', views.CarteleraHorarioView.as_view(), name='api.cartelera.horario'),
    url(r'^cartelera/(?P<cine>\d+)/(?P<pelicula>\d+)/?$', views.CarteleraDayView.as_view(), name='api.cartelera.dia'),
    url(r'^cine/?$', views.CineView.as_view(), name='api.cine'),
    url(r'^$', views.IndexView.as_view(), name='api.index'),
]
