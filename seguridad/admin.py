from django.contrib import admin

from seguridad.models import Modulo, ModuloGrupo,Empleado,Fotouser

admin.site.register(Modulo)
admin.site.register(Empleado)

admin.site.register(ModuloGrupo)

admin.site.register(Fotouser)
# Register your models here.
