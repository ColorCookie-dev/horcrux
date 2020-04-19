from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Organisation
from django import forms
from django.core.exceptions import ValidationError


class CreateUserForm(forms.Form):
    username = forms.CharField(label='Username', min_length=4, max_length=150)
    firstname = forms.CharField(label='Firstname', min_length=4, max_length=150)
    lastname = forms.CharField(label='Lastname', min_length=4, required=False, max_length=150)
    email = forms.EmailField(label='email')

    org = forms.ModelChoiceField(queryset=Organisation.objects.all())
    phone = forms.IntegerField(label='phone number')
    postcode = forms.IntegerField(label='PostCode')
    addr = forms.CharField(label='Address')

    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
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

    def clean_postcode(self):
        postcode = self.cleaned_data['postcode']
        if len(str(postcode)) != 6:
            raise ValidationError('Length of PostCode should be 6')
        return postcode
 
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
            phone=self.cleaned_data['phone'],
            postcode=self.cleaned_data['postcode'],
            addr=self.cleaned_data['addr']
        )
        return user
