from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Car, CarInventory
from django.db.models import Sum


@receiver([post_save, post_delete], sender=Car)
def car_post_save(sender, instance, **kwargs):
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value,
    )
