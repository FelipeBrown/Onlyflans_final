from django.contrib import admin
from .models import CalificacionFlan, Flan, Contacto

# Register your models here.

admin.site.register(Flan)
admin.site.register(Contacto)
admin.site.register(CalificacionFlan)