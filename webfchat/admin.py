from django.contrib import admin

# Register your models here.
from .models import FchatWebsite

class FchatWebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'environment', 'created_at', 'updated_at')
    list_filter = ('environment', 'created_at', 'updated_at')
    search_fields = ('name', 'description') 

admin.site.register(FchatWebsite, FchatWebsiteAdmin)