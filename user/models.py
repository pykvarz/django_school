from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
	is_admin = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	surname = models.CharField(max_length=255, null=True, blank=True)


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	iin = models.IntegerField(blank=True, null=True)




