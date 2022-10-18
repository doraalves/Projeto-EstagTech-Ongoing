from ongoingfront.models import Usuario
from django.contrib import admin

@admin.register(Usuario)
class OngoingfrontAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'email', 'turno', 'status')
    search_fields = ('nome', 'cargo', 'email',)