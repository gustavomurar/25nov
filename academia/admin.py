from django.contrib import admin
from .models import Formacao
from .models import Instituicao, Instrutor


admin.site.register(Formacao)
admin.site.register(Instituicao)
admin.site.register(Instrutor)