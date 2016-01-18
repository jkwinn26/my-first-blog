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
    returned_date = models.DateTimeField(blank=True, null=True)
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

class Department(models.Model):
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50, blank=False, null=False)
    supervisor = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.name

# Employee Model (for New Employee Form)
# TODO: do one-to-one association with auth.user
# (& with AD auth, this can be a one-stop-shop to create AD accounts/new employees).
class Employee(models.Model):
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    CONTRACTOR_FULL_TIME = 'CF'
    CONTRACTOR_PART_TIME = 'CP'
    STUDENT_FULL_TIME = 'SF'
    STUDENT_PART_TIME = 'SP'
    TYPE_CHOICES = (
        (FULL_TIME, 'Full-time'),
        (PART_TIME, 'Part-time'),
        (CONTRACTOR_FULL_TIME, 'Contractor full-time'),
        (CONTRACTOR_PART_TIME, 'Contractor part-time'),
        (STUDENT_FULL_TIME, 'Student full-time'),
        (STUDENT_PART_TIME, 'Student part-time'),
    )
    employee_id = models.CharField(max_length=5, blank=False, null=False, primary_key=True) #00000
    last_name = models.CharField(max_length=75, blank=False, null=False)
    first_name = models.CharField(max_length=75, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=False, null=False)
    job_title = models.CharField(max_length=50, blank=False, null=False)
    emp_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=FULL_TIME)
    department = models.ForeignKey('esat.Department')
    new_phone = models.BooleanField(default=False)
    outside_line = models.BooleanField(default=False)
    phone_extn = models.PositiveSmallIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=False)
    work_location = models.CharField(max_length=50, blank=True, null=False)
    termination_date = models.DateField(null=True, blank=True)
    termination_cause = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name + "(" + self.employee_id + ")"
        
#TODO: add tie-ins for CPSI/Evident, AD/Windows, Exchange/Outlook, PACS, Orchard