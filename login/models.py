from django.db import models


# Create your models here.
class AccountUser(models.Model):
    account_holder=models.CharField(max_length=200,null=True)
    holder_org_name=models.CharField(max_length=200,null=True)
    org_fax=models.FloatField(max_length=10,null=True)

    org_CIN_number=models.CharField(max_length=200,null=True)
