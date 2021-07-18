from django.contrib import admin
from .models import Dsuser

# Register your models here.
class DsuserAdmin(admin.ModelAdmin):
    list_display = ('id', 'password')

admin.site.register(Dsuser, DsuserAdmin)