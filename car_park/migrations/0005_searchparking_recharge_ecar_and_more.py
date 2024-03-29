# Generated by Django 4.0.5 on 2022-08-19 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car_park', '0004_alter_booking_end_date_alter_booking_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchparking',
            name='recharge_ecar',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='registration_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='comment',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profileavatar',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/avatar/'),
        ),
        migrations.AlterField(
            model_name='profileavatar',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
