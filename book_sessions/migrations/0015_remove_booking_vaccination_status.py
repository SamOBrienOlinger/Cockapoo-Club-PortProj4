# Generated by Django 4.1.3 on 2023-01-13 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_sessions', '0014_remove_booking_vaccinated_yes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Vaccination_Status',
        ),
    ]
