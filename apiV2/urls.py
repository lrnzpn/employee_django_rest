from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apiV2 import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
    path('employee/<int:pk>/', views.EmployeeObject.as_view()),
]
