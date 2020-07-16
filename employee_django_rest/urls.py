"""employee_django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

# router = DefaultRouter()
# router.register(r'employees', views.EmployeeViewSet)
# router.register(r'employee', views.EmployeeViewSet)


schema_view = get_schema_view(title='Employees API',
                description='An API to create, edit, delete profiles of employees.')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='Employee API')),
    # path('api/', include('api.urls')),
    path('api/v2/', include('apiV2.urls')),
]
