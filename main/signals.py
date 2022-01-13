from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order


@receiver(post_save, sender=Order)
def created_order(sender, instance, created, **kwargs):
    if created:
        instance.status = "created"
        instance.save()
