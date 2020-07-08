from django.contrib import admin
from deportes.models import Estado


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'abreviado')
