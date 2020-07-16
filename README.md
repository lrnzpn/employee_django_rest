# Django REST API
---
### This API is used with the employee_react repository

To use the following API, do the following:

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 5000
```

**Note: It is important we run it with port 5000 because that what's set in the frontend**

Endpoints:
```
Get all employees: http://localhost:5000/api/v2/employees/
Employee object: http://localhost:5000/api/v2/employee/:id
```
