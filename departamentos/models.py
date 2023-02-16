from django.db import models

class Departamentos(models.Model):
    nome = models.CharField(max_length=50, help_text="Nome do Departamento")

    def __str__(self):
        return self.nome