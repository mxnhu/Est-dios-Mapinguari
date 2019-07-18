from django.conf import settings
from django.db import models
from django.utils import timezone
import pandas as pd

class Session(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

class Dados(models.Model):
	data = pd.DataFrame()

class Retorno(models.Model):
	mapaRisco = pd.DataFrame()
	mapaFreq = pd.DataFrame()