# Generated by Django 4.1.3 on 2022-12-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_sessions', '0005_photo_booking_date_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=''),
            # field=models.DateField(default='YYYY-MM-DD'),
            # # field=models.DateField(input_formats=['%d/%m/%Y'])
            # field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(default='00:00'),
        ),
    ]
