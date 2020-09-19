from django.contrib import admin

# Register your models here.
from .models import Setting, ContactMessage


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company','update_at',  'status']
    list_filter = ['company']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status']
    list_filter = ['status']
    readonly_fields = ('name', 'email','subject','message','ip')


admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactMessage,ContactAdmin)