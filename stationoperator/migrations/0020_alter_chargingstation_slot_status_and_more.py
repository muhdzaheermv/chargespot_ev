# Generated by Django 5.0 on 2024-09-21 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationoperator', '0019_alter_chargingstation_slot_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='slot_status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('in_review', 'in Review'), ('disabled', 'Disabled'), ('draft', 'Draft'), ('published', 'Published')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='station', to='stationoperator.vendor'),
        ),
        migrations.AlterField(
            model_name='slotreservation',
            name='slot_status',
            field=models.CharField(choices=[('reserved', 'Slot Reserved'), ('in_process', 'Booking in Process'), ('completed', 'Charging Completed')], default='Booking in Process', max_length=30),
        ),
        migrations.AlterField(
            model_name='stationreview',
            name='rating',
            field=models.IntegerField(choices=[(2, '⭐⭐☆☆☆'), (3, '⭐⭐⭐☆☆'), (4, '⭐⭐⭐⭐☆'), (5, '⭐⭐⭐⭐⭐'), (1, '⭐☆☆☆☆')], default=None),
        ),
    ]
