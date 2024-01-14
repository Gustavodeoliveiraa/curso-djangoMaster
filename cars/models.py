from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.brand


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=255)
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='car_brand'
    )
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self) -> str:
        return self.model
