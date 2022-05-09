import django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Pagos(models.Model):
    name=models.TextField(max_length=30)
    creador=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    valor=models.IntegerField()

    def __str__(self) -> str:
        return f'Pagos de {self.creador.username}'

class Cuentas(models.Model):

    name=models.CharField(max_length=30)    
    colaboradores=models.ManyToManyField(User)
    pagos=models.ManyToManyField(Pagos)
    fecha_de_creado=models.DateField(default=timezone.now)

    def __str__(self) -> str:
        # return '-'.join([str(colaboradores.username) for colaboradores in self.colaboradores.all()])
        return self.name


