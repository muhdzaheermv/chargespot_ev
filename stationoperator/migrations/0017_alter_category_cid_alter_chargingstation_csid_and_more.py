# Generated by Django 5.0 on 2024-09-21 19:19

import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationoperator', '0016_alter_category_cid_alter_chargingstation_slot_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdef123', length=10, max_length=20, prefix='cat', unique=True),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='csid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcde12', length=10, max_length=20, prefix='', unique=True),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='slot_status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('in_review', 'in Review'), ('disabled', 'Disabled'), ('draft', 'Draft'), ('published', 'Published')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='slotreservation',
            name='slot_status',
            field=models.CharField(choices=[('in_process', 'Booking in Process'), ('reserved', 'Slot Reserved'), ('completed', 'Charging Completed')], default='Booking in Process', max_length=30),
        ),
        migrations.AlterField(
            model_name='stationreview',
            name='rating',
            field=models.IntegerField(choices=[(1, '⭐☆☆☆☆'), (4, '⭐⭐⭐⭐☆'), (5, '⭐⭐⭐⭐⭐'), (2, '⭐⭐☆☆☆'), (3, '⭐⭐⭐☆☆')], default=None),
        ),
    ]
