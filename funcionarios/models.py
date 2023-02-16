from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do Funcionário")

    def __str__(self):
        return self.nome
