from django.contrib import admin
from contactenquiry.models import Contactenquiry

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']

admin.site.register(Contactenquiry, ContactAdmin)