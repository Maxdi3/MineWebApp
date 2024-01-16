from django.contrib import admin
from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'machine_name', 'location_long', 'location_lat', ]

# Register your models here.
admin.site.register(Users, UsersAdmin)