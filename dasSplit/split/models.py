from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Cuentas(models.Model):

    name=models.CharField(max_length=30)    
    colaboradores=models.ManyToManyField(User)
    fecha_de_creado=models.DateField(default=timezone.now)

    def __str__(self) -> str:
        # return '-'.join([str(colaboradores.username) for colaboradores in self.colaboradores.all()])
        return self.name


class Pagos(models.Model):

    name=models.CharField(max_length=30)
    creador=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    cuentas=models.ForeignKey(Cuentas,on_delete=models.CASCADE,null=True)
    valor=models.IntegerField()

    def __str__(self) -> str:
        return self.name




