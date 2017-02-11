from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic import ListView

from pelicula.models import Pelicula
from website.forms import LoginForm
from cartelera.models import Cine

class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super(Home, self).get_context_data(**kwargs)
        contexto['peliculas'] = Pelicula.objects.all().order_by('id')
        return contexto

class DetallePelicula(DetailView):
    template_name = 'pelicula.html'
    model = Pelicula

    def get_context_data(self, **kwargs):
        contexto = super(DetallePelicula, self).get_context_data(**kwargs)
        contexto['cines'] = Cine.objects.all().order_by('nombre')
        return contexto

class ListadoCine(ListView):
    template_name = 'cine.html'
    model = Cine

class Login(FormView):
    template_name= 'login.html'
    form_class= LoginForm

    def form_valid(self, form):
        usuario=  form.cleaned_data['usuario']
        login(self.request, usuario)
        return redirect('home')