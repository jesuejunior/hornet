from django.contrib import admin

# Register your models here.

from models import *


class ApplianceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')
    list_filter = ('type', )


class PlugAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'room', 'appliance', 'connected', 'priority')
    list_filter = ('room', 'connected', 'priority')


class UsageAdmin(admin.ModelAdmin):
    list_display = ('id', 'plug', 'registered', 'total_usage')
    list_filter = ('plug', 'registered')


class ResidenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'cep', 'address')

admin.site.register(Appliance, ApplianceAdmin)
admin.site.register(Plug, PlugAdmin)
admin.site.register(Usage, UsageAdmin)
admin.site.register(Residence, ResidenceAdmin)