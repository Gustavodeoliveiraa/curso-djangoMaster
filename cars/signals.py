from django.db.models.signals import (
    pre_save, pre_delete, post_save, post_delete
)
from django.dispatch import receiver
from .models import Car


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('### PRÉ SAVE ###')
    print(instance.model)


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('### POST SAVE ###')


@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print('### PRÉ DELETE ###')


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('### POST DELETE ###')
