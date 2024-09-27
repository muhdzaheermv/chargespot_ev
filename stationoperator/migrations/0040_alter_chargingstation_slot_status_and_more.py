# Generated by Django 5.0 on 2024-09-26 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationoperator', '0039_alter_chargingstation_slot_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='slot_status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft'), ('disabled', 'Disabled'), ('in_review', 'in Review'), ('rejected', 'Rejected')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='slotreservation',
            name='slot_status',
            field=models.CharField(choices=[('completed', 'Charging Completed'), ('reserved', 'Slot Reserved'), ('in_process', 'Booking in Process')], default='Booking in Process', max_length=30),
        ),
        migrations.AlterField(
            model_name='stationreview',
            name='rating',
            field=models.IntegerField(choices=[(4, '⭐⭐⭐⭐☆'), (3, '⭐⭐⭐☆☆'), (2, '⭐⭐☆☆☆'), (5, '⭐⭐⭐⭐⭐'), (1, '⭐☆☆☆☆')], default=None),
        ),
    ]
