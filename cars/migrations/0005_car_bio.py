# Generated by Django 5.0.1 on 2024-01-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
