from django.db import models

class Address(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=50) # Rua
    bairro = models.CharField(max_length=30)
    localidade = models.CharField(max_length=30) # Cidade
    uf = models.CharField(max_length=2) # Estado
# Create your models here.