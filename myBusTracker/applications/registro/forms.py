from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
user = get_user_model()

class RegistroFormulario(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'name',
            'username',
            'email',
            'password1',
            'password2'
        ]