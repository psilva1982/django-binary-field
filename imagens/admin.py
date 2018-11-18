from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib import admin
from django.urls import reverse
from django.template.defaultfilters import filesizeformat

from .forms import ClienteForm
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):

    form = ClienteForm
    list_display = ['first_name', 'download']
    ordering = ['first_name']
    search_fields = ['first_name']
    
    @mark_safe
    def download(self, obj):
        href = reverse('foto-cliente', args=[obj.id])
        return '<a href="{}" target="_blank">Visualizar</a>'.format(href)
    download.allow_tags = True
    download.short_description = 'Foto'


    def get_queryset(self, request):
        qs = super(ClienteAdmin, self).get_queryset(request)
        qs = qs.defer('foto')
        return qs

# Register your models here.
admin.site.register(Cliente, ClienteAdmin) 