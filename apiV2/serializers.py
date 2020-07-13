from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
      model = Employee
      fields = '__all__'
      
  def to_representation(self, instance):
    return {
      'employee_id': instance.employee_id,
      'personal_details': {
        'first_name': instance.first_name,
        'last_name': instance.last_name,
        'middle_name': instance.middle_name,
        'gender': instance.gender,
        'title': instance.title,
        'address': {
          'unit_number': instance.unit_number,
          'street': instance.street,
          'city': instance.city,
          'province': instance.province,
          'region': instance.region,
          'zip_code': instance.zip_code,
        },
        'contact': {
          'landline_number': instance.landline_number,
          'mobile_number': instance.mobile_number,
          'email': instance.email,
        },
      },
      'job_details' :{
        'title': instance.job_title,
        'employee_number': instance.employee_number,
        'location': instance.location,
        'department': instance.department,
        'email': instance.job_email,
        'salary': instance.salary,
      },
      'benefits_details': {
        'SSS': instance.sss,
        'PhilHealth' : instance.philhealth,
        'PAGIBIG': instance.pagibig,
        'BIR' : instance.bir,
      },
      'date': instance.date,
      'updated':instance.updated
      
    }