import mimetypes
import time

from django.http.response import HttpResponseNotModified, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.http import http_date
from django.views.generic.base import View
from django.views.static import was_modified_since

from .models import Cliente

class ClienteFotoView(View):

    def get(self, request, name):
        foto_cliente = get_object_or_404(Cliente.objects.defer('foto'))
                
        response = HttpResponse(foto_cliente.foto, content_type='image/jpeg')
        response['Content-Encoding'] = 'image/jpeg'
        return response
