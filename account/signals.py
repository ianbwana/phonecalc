from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import Account


@receiver(post_save, sender=Account)
def create_user_token(sender, instance, created=False, **kwargs):
    try:
        Token.objects.create(user=instance)

    except Exception as e:
        print(e)
