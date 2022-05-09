from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    """Pre.built model user"""
    email = forms.EmailField(required=True)

    class Meta:
        """campos que queramos que aparezca en el form"""
        model = User
        fields = ("username", "email", "password1", "password2") 
        help_text={k:"" for k in fields}

    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

