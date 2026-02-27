from django.contrib import admin
from .models import Abuneci, ElaqeMesaji


@admin.register(Abuneci)
class AbunecilAdmin(admin.ModelAdmin):
    list_display = ['email', 'tarix']
    search_fields = ['email']
    readonly_fields = ['tarix']
    list_filter = ['tarix']


@admin.register(ElaqeMesaji)
class ElaqeMesajiAdmin(admin.ModelAdmin):
    list_display = ['ad', 'email', 'tarix', 'oxunub']
    search_fields = ['ad', 'email', 'mesaj']
    list_filter = ['oxunub', 'tarix']
    readonly_fields = ['tarix']
    list_editable = ['oxunub']
