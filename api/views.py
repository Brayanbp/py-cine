from django.http import JsonResponse
from django.views import View
import json
from django.core.serializers.json import DjangoJSONEncoder

from cartelera.models import Cartelera


class CarteleraDayView(View):
    def get(self, request, cine, pelicula):
        try:
            response = {
                "state": 1,
                "msg": "OK"
            }

            datacartelera = Cartelera.objects.filter(cine__id__exact=cine).filter(pelicula__id__exact=pelicula).values('fecha')
            datacartelera.query.group_by = ['fecha']
            response["data"] = list(datacartelera)
        except Exception as err:
            response["state"]= 0
            response["msg"]= str(err)

        return JsonResponse(response)


class CarteleraHorarioView(View):
    def get(self, request, cine, pelicula, fecha):
        try:
            response = {
                "state": 1,
                "msg": "OK"
            }

            datacartelera = Cartelera.objects.filter(cine__id__exact=cine).filter(pelicula__id__exact=pelicula).filter(fecha__exact=fecha).values('id', 'hora')
            response["data"] = list(datacartelera)
        except Exception as err:
            response["state"]= 0
            response["msg"]= str(err)

        return JsonResponse(response)


class CineView(View):
    def get(self, request):
        return JsonResponse({'success': False})


class IndexView(View):
    def get(self, request):
        return JsonResponse({'success': True})