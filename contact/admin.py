from django.contrib import admin
from .models import Contact
# Register your models here.


class contactAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name", "email", "message")


admin.site.register(Contact, contactAdmin)
