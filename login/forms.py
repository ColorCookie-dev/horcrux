from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Organisation
from django import forms
from django.core.exceptions import ValidationError


class CreateUserForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)

    firstname = forms.CharField(label='Enter Firstname', min_length=4, max_length=150)
    lastname = forms.CharField(label='Enter Lastname', min_length=4, required=False, max_length=150)

    org = forms.ModelChoiceField(queryset=Organisation.objects.all())

    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
 
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower().strip()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['firstname'],
            last_name=self.cleaned_data['lastname'],
            email=self.cleaned_data['email'],
            org=self.cleaned_data['org'],
            password=self.cleaned_data['password1'],
        )
        return user
