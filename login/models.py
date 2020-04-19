from django_cryptography.fields import encrypt
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Organisation(models.Model):
    name = models.CharField(_("organisation name"), max_length=100, unique=True, blank=False)
    email = models.EmailField(_("email address"), unique=True)
    VAT = encrypt(models.IntegerField(_("VAT number")))
    phone = encrypt(models.IntegerField(_("phone number")))
    website = encrypt(models.URLField(_("website")))
    CIN = encrypt(models.IntegerField(_("CIN number")))
    postcode = encrypt(models.IntegerField(_("postcode")))
    addr = encrypt(models.CharField(_("address"), max_length=500))

    def __str__(self):
        return self.name

class User(AbstractUser):
    org = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    phone = encrypt(models.IntegerField(_("phone")))
    postcode = encrypt(models.IntegerField(_("postcode")))
    addr = encrypt(models.CharField(_("address"), max_length=500))

