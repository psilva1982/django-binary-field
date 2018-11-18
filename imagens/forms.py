from django import forms
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Cliente

class ClienteForm(forms.ModelForm):

    #file = forms.FileField(widget=DBFileWidget())
    foto = forms.ImageField()

    class Meta:
        model = Cliente
        fields = ['first_name']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)

        instance = kwargs.get('instance')
        field = self.fields['foto']
        field.widget.instance = instance
        if instance: field.required = False

    def save(self, commit=True):
        db_file = super(ClienteForm, self).save(commit=False)
        foto = self.cleaned_data.get('foto')
        if foto:
            db_file.foto = foto.read()
        if commit:
            db_file.save()
        return db_file