from django.contrib import admin
from .models import AssetType, Asset, Department, Employee

# Register your models here.
class AssetAdmin(admin.ModelAdmin):
    list_display = ('tag', 'type', 'assigned_user')
    list_filter = ('type', 'assigned_user')
    search_fields = ['tag']
    #fields = ('tag', 'type', 'assigned_user')

admin.site.register(AssetType)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Department)
admin.site.register(Employee)