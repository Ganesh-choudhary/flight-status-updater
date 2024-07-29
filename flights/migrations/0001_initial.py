# Generated by Django 5.0.7 on 2024-07-29 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=50)),
                ('gate', models.CharField(max_length=10)),
                ('scheduled_time', models.DateTimeField()),
                ('estimated_time', models.DateTimeField()),
                ('notification_sent', models.BooleanField(default=False)),
            ],
        ),
    ]