from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='employee_images/', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username