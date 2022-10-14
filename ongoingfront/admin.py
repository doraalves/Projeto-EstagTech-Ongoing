from ongoingfront.models import Usuario
from django.contrib import admin

@admin.register(Usuario)
class OngoingfrontAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'email', 'turno', 'status')
    readonly_fields = ('senha',)
    search_fields = ('nome', 'cargo', 'email',)