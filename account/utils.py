# from django.core.mail import send_mail
#
#
# def send_activation_mail(email, activation_code):
#     message = f"""Спасибо за регистрацию. Активируйте аккаунт по ссылке:
#     http://127.0.0.1:8000/accounts/activation/?u={activation_code}"""
#     send_mail(
#         'Активация аккаунта',
#         message,
#         'test@mysite.com',
#         [email, ]
#     )

# АТАЙ, АСКАТ, снизу код взят из signals.py файла из того документа
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserAccount


# signal that gets fired after the user is saved
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserAccount.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()