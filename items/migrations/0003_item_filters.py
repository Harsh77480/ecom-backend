# Generated by Django 5.0.1 on 2024-02-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_values_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='filters',
            field=models.ManyToManyField(to='items.filter'),
        ),
    ]
