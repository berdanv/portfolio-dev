from django.db import models


class Alunos(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
    idade = models.IntegerField()