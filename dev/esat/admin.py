from django.contrib import admin
from .models import AssetType, Asset, Department, Employee, SoftwareVendor, SoftwarePackage

# Register your models here.
class AssetAdmin(admin.ModelAdmin):
    list_display = ('tag', 'type', 'assigned_user')
    list_filter = ('type', 'assigned_user')
    search_fields = ['tag']
    #fields = ('tag', 'type', 'assigned_user')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'supervisor', 'number')
    #list_filter = ('name', 'supervisor', 'number')
    search_fields = ['name', 'supervisor', 'number']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'last_name', 'first_name', 'department', 'start_date')
    list_filter = (
        ('department', admin.RelatedOnlyFieldListFilter),
    )
    #raw_id_admin = ('department')
    search_fields = ['employee_id', 'last_name', 'first_name']

admin.site.register(AssetType)
admin.site.register(Asset, AssetAdmin)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)

admin.site.register(SoftwareVendor)
admin.site.register(SoftwarePackage)