from django.db import models

# Create your models here.
class Usuario(models.Model):
    # cargo_choices = (
    #     ("Dev", "Desenvolvedor"),
    #     ("Ana", "Analista")
    # ),

    # status_choices = (
    #     ("T1", "T1"),
    #     ("T2", "T2"),
    #     ("T3", "T3"),
    #     ("Comercial", "Comercial")
    # ),

    # turn_choices = (
    #     ("On", "Online"),
    #     ("Off", "Offline"),
    #     ("Ausente", "Ausente"),
    #     ("Almoço", "Almoço"),
    #     ("Férias", "Férias"),
    #     ("Treinamento", "Treinamento")
    # )

    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    senha = models.CharField(max_length=100)

    cargo = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)