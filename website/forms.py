from django.contrib.auth import authenticate
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'validate'}))

    def clean(self):
        usuario_ = self.cleaned_data.get('username')
        password_ = self.cleaned_data.get('password')

        usuario_auth = authenticate(username=usuario_, password=password_)
        if not usuario_auth:
            raise forms.ValidationError('Credenciales inválidas')
        else:
            self.cleaned_data['usuario'] = usuario_auth

        return self.cleaned_data