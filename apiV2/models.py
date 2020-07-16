from django.db import models

# Create your models here.
class Employee(models.Model):
  employee_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=255, blank=True)
  last_name = models.CharField(max_length=255, blank=True)
  middle_name = models.CharField(max_length=255, blank=True)
  gender = models.CharField(max_length=10, blank=True)
  title = models.CharField(max_length=40, blank=True)
  # address
  unit_number = models.IntegerField(default=0)
  street = models.CharField(max_length=255, blank=True)
  city = models.CharField(max_length=40, blank=True)
  province = models.CharField(max_length=255, blank=True)
  region = models.CharField(max_length=255, blank=True)
  zip_code = models.IntegerField(default=0)
  # contact details
  landline_number = models.IntegerField(default=0)
  mobile_number = models.IntegerField(default=0)
  email = models.EmailField(max_length=255, blank=True)
  # job details 
  job_title = models.CharField(max_length=255, blank=True)
  employee_number = models.IntegerField(default=0)
  location = models.CharField(max_length=255, blank=True)
  department = models.CharField(max_length=255, blank=True)
  job_email = models.EmailField(max_length=255, blank=True)
  salary = models.IntegerField(default=0)
  # benefits details
  sss = models.CharField(max_length=255, blank=True)
  philhealth = models.CharField(max_length=255, blank=True)
  pagibig = models.CharField(max_length=255, blank=True)
  bir = models.CharField(max_length=255, blank=True)
  
  date = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)