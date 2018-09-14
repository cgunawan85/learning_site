from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]

    def clean_password1(self):
        data = self.cleaned_data['password1']
        if len(data) < 8:
            raise forms.ValidationError("Please choose a password that is at least 8 characters long")
        return data
