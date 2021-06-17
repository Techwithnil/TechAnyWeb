
from django.contrib import admin
from registration.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image']

admin.site.register(Profile,ProfileAdmin)
