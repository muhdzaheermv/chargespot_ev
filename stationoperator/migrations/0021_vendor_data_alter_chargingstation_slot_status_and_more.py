# Generated by Django 5.0 on 2024-09-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationoperator', '0020_alter_chargingstation_slot_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='data',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='slot_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('in_review', 'in Review'), ('disabled', 'Disabled'), ('published', 'Published'), ('rejected', 'Rejected')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='slotreservation',
            name='slot_status',
            field=models.CharField(choices=[('in_process', 'Booking in Process'), ('completed', 'Charging Completed'), ('reserved', 'Slot Reserved')], default='Booking in Process', max_length=30),
        ),
        migrations.AlterField(
            model_name='stationreview',
            name='rating',
            field=models.IntegerField(choices=[(4, '⭐⭐⭐⭐☆'), (1, '⭐☆☆☆☆'), (2, '⭐⭐☆☆☆'), (3, '⭐⭐⭐☆☆'), (5, '⭐⭐⭐⭐⭐')], default=None),
        ),
    ]
