from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Pocket,Charge,Payment

class NewUserForm(UserCreationForm):
    """built-in model user"""

    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        
      super().__init__(*args, **kwargs)
      self.fields['password1'].help_text='Enter the password with at least 8 digits'
      self.fields['password2'].help_text='Enter the same password, to verify'


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


class PocketForm(forms.ModelForm):

    name=forms.CharField(required=True,label='Name of Pocket',)

    class Meta:
        model = Pocket
        fields= ['name']

class PaymentForm(forms.ModelForm):

    value=forms.IntegerField(required=True,label='Value of payment',)

    class Meta:
        model = Payment
        fields= ['value','pocket']
        widgets={'pocket':forms.Select(attrs={'class':'form-control'})}
        