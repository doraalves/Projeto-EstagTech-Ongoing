from unicodedata import name
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    senha = models.CharField(max_length=100)