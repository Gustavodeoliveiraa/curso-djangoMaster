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


# @receiver(pre_save, sender=Car)
# def car_pre_save(sender, instance, **kwargs):
#     if not instance.bio:
#         ia_bio = get_car_ai_bio(
#             instance.model,
#             instance.brand,
#             instance.model_year
#         )
#         instance.bio = ia_bio
