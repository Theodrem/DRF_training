from typing import ChainMap
from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.lookups import In

# Create your models here.

class Hero(models.Model):
    name = CharField(max_length=50, unique=True)
    attack = IntegerField()
    life = IntegerField()
    origin = CharField(max_length=20)

