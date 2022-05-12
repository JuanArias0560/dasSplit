from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Cuentas

class NewUserForm(UserCreationForm):
    """built-in model user"""

    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        
      super().__init__(*args, **kwargs)
      self.fields['password1'].help_text='Ingresa una clave de por lo menos 8 digitos'
      self.fields['password2'].help_text='Ingresa la misma clave escrita anteriormente, para verificar'


    class Meta:
        """campos que queramos que aparezca y no aparezcan en el form"""

        model = User
        fields = ("username", "email", "password1", "password2") 
        help_texts = {
            
            'username': None,
            'email': None,
            
        }


    def save(self,commit=True):

        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CuentasForm(forms.ModelForm):

    name=forms.CharField(required=True,label='Nombre de la cuenta',)

    class Meta:
        model = Cuentas
        fields= ['name']