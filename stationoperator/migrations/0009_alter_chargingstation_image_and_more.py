# Generated by Django 5.0 on 2024-09-19 13:02

import stationoperator.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationoperator', '0008_alter_chargingstation_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='image',
            field=models.ImageField(default='station.jpg', upload_to=stationoperator.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='slot_status',
            field=models.CharField(choices=[('in_review', 'in Review'), ('published', 'Published'), ('draft', 'Draft'), ('disabled', 'Disabled'), ('rejected', 'Rejected')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='slotreservation',
            name='slot_status',
            field=models.CharField(choices=[('completed', 'Charging Completed'), ('in_process', 'Booking in Process'), ('reserved', 'Slot Reserved')], default='Booking in Process', max_length=30),
        ),
        migrations.AlterField(
            model_name='stationreview',
            name='rating',
            field=models.IntegerField(choices=[(1, '⭐☆☆☆☆'), (4, '⭐⭐⭐⭐☆'), (3, '⭐⭐⭐☆☆'), (2, '⭐⭐☆☆☆'), (5, '⭐⭐⭐⭐⭐')], default=None),
        ),
    ]
