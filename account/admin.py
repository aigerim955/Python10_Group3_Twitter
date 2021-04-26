from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import UserAccount
# User = get_user_model()
admin.site.register(UserAccount)

