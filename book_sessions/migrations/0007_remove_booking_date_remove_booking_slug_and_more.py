# Generated by Django 4.1.3 on 2022-12-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_sessions', '0006_alter_booking_date_alter_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='title',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='session_type',
            field=models.CharField(choices=[('O', 'One to One training session'), ('G', 'Group training session')], default='O', max_length=1),
        ),
    ]
