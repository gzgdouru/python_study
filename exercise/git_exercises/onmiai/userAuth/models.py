from django.db import models

# Create your models here.
class Boy(models.Model):
    nickname = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class Girl(models.Model):
    nickname = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class B2G(models.Model):
    b = models.ForeignKey(to="Boy", to_field="id", on_delete=models.DO_NOTHING)
    g = models.ForeignKey(to="Girl", to_field="id", on_delete=models.DO_NOTHING)