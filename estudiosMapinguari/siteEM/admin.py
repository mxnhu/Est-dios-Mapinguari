from django.contrib import admin
from .models import Session
from .models import Dados
from .models import Retorno

admin.site.register(Session)
admin.site.register(Dados)
admin.site.register(Retorno)