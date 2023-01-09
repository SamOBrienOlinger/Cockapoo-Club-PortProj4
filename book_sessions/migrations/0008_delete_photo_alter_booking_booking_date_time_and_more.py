# Generated by Django 4.1.3 on 2023-01-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_sessions', '0007_remove_booking_date_remove_booking_slug_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='confirmed',
            field=models.BooleanField(default=True),
        ),
    ]
