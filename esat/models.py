from django.db import models
from django.utils import timezone

# Allow admins to define Asset Types
class AssetType(models.Model):
    type = models.CharField(max_length=25,
            blank=False, null=False)
    description = models.CharField(max_length=100,
            blank=False, null=False)
    
    def __str__(self):
        return self.type

class Asset(models.Model):
    #name = models.CharField(max_length=75 
    #        blank=False, null=False)
    tag = models.CharField(max_length=25,
            blank=False, null=False)
    type = models.ForeignKey('esat.AssetType',
            related_name='asset_type')
    created_by = models.ForeignKey('auth.user')
    created_date = models.DateTimeField(
            default=timezone.now)
    purchase_date = models.DateTimeField(blank=True, null=True)
    #description = models.CharField()
    make = models.CharField(max_length=25, blank=True, null=False)
    model = models.CharField(max_length=25, blank=True, null=False)
    assigned_user = models.ForeignKey('auth.user',
            blank=True, null=True, related_name='asset_owner')
    issued_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    decommission_date = models.DateField(blank=True, null=True)
    
    def is_active(self):
        return self.active
    
    def decommission(self):
        self.active = False
        decommission_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.tag + "(" + str(self.type) + ")"
