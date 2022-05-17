from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(default='racoon.jpg')

    def __str__(self) -> str:
        return f'Perfil de {self.user.username}'


class Pocket(models.Model):

    CATEGORIES=(
        ('trip','trip'),
        ('home','home'),
        ('couple','couple'),
        ('friends','friends'),
        ('other','other'),
        )

    name=models.CharField(max_length=30) 
    author=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='author')   
    user=models.ManyToManyField(User,related_name="pocket")
    categories=models.CharField(max_length=255,choices=CATEGORIES,null=True)
    date=models.DateTimeField(default=timezone.now)    


    def __str__(self) -> str:        
        return self.name


class Payment(models.Model):

    
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="payment")
    pocket=models.ForeignKey(Pocket,on_delete=models.CASCADE,null=True)
    value=models.IntegerField()
    date=models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return 'payment'

class Charge(models.Model):

    name=models.CharField(max_length=30)
    value=models.IntegerField()    
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="charge")
    pocket=models.ForeignKey(Pocket,on_delete=models.CASCADE,null=True)
    date=models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.name








