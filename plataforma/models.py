from django.db import models

# Create your models here.
class Carteira(models.Model):
    nome = models.CharField(max_length=64, blank=False, null=False)
    email = models.EmailField(max_length=64, blank=False, null=False)
    cpf = models.IntegerField(blank=False, null=False)
    matricula = models.IntegerField(blank=False, null=False)
    # para a associacao, irá ser colocado o id da carteirinha
    # associacao = models.IntegerField(blank=False, null=False)
    data_nasc = models.DateField(blank=False, null=False)
    data_exped = models.DateField(blank=False, null=False)
    data_valid = models.DateField(blank=False, null=False)
    foto = models.ImageField(upload_to='carteiras')

    def __str__(self):
        return self.nome