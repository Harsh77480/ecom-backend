# Generated by Django 5.0.1 on 2024-02-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_brandvalues_category_colorvalues_fabricvalues_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='original_price',
            field=models.FloatField(default=0),
        ),
    ]