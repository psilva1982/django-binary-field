from django.db import models

# Create your models here.
class Cliente(models.Model):
     first_name = models.CharField(max_length=30)
     foto = models.BinaryField(editable=True)