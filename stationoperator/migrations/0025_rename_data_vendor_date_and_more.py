# Generated by Django 5.0 on 2024-09-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationoperator', '0024_vendor_cover_image_alter_chargingstation_slot_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='data',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='slot_status',
            field=models.CharField(choices=[('in_review', 'in Review'), ('draft', 'Draft'), ('rejected', 'Rejected'), ('disabled', 'Disabled'), ('published', 'Published')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='stationreview',
            name='rating',
            field=models.IntegerField(choices=[(4, '⭐⭐⭐⭐☆'), (5, '⭐⭐⭐⭐⭐'), (2, '⭐⭐☆☆☆'), (3, '⭐⭐⭐☆☆'), (1, '⭐☆☆☆☆')], default=None),
        ),
    ]
