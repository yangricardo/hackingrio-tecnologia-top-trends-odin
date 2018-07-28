from django.db import models
from django.contrib.auth.models import User

class Beneficiary(models.Model):

    nome = models.CharField(max_length=200,)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Donation(models.Model):

    doado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    valor_doado = models.DecimalField(max_digits=10, decimal_places=2 )
    data = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.valor_doado)


# Create your models here.
class DonatedBeneficiary(models.Model):

    doacao = models.ForeignKey(Donation,  on_delete=models.DO_NOTHING)
    valor_doado_ao_beneficiario = models.DecimalField(max_digits=10, decimal_places=2)
    beneficiario = models.ForeignKey(Beneficiary,  on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.valor_doado_ao_beneficiario)

