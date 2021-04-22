from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, primary_key=True)
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True)
