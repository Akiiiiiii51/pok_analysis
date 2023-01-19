from django.contrib import admin
from .models import App

# Register your models here.
class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(App, AppAdmin)