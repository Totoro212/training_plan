from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
    )
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already registered")
        return email