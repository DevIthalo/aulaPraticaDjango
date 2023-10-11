from django.db import models
from django.contrib.postgres.fields import ArrayField

class MeContrate(models.Model):
    servico = models.CharField(max_length=150, null=False)
    nome = models.CharField(max_length=40, null=False)
    email = models.CharField(max_length=45, null=False)
    mensagem = models.TextField()
    lido = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'Ofertas de contrato'
        verbose_name_plural = 'Ofertas de contrato'
        
