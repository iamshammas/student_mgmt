from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# role (Admin/Student)
# roll number
# department
# year of admission


# class Profile(models.Model):
#     class Role(models.TextChoices):
#         ADMIN = 'ADMIN', 'Admin'
#         STUDENT = 'STUDENT', 'Student'
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=50, choices=Role.choices, default=Role.STUDENT)
#     roll_no = models.IntegerField()
#     dept = models.CharField(max_length=200)
#     admission_year = models.IntegerField()

#     def __str__(self):
#         return self.user.username
    
