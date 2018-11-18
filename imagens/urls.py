import re

from django.conf import settings
from django.conf.urls import url

from imagens import views


def foto_cliente(prefix=settings.MEDIA_URL, view=views.ClienteFotoView.as_view(), name='foto-cliente', **kwargs):
    prefix = re.escape(prefix.lstrip('/'))
    return url(r'^{}(?P<name>.*)$'.format(prefix), view, name=name, kwargs=kwargs)


urlpatterns = [
    foto_cliente('foto/'),
]