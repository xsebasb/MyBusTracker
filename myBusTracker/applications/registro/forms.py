from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate

user = get_user_model()

class UsuarioLoginFormulario(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Este usuario No existe")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("Este usuario no esta activo")

        return super(UsuarioLoginFormulario, self).clean(*args, **kwargs )

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