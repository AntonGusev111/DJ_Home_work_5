# Generated by Django 4.0.3 on 2022-04-11 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_alter_measurement_temperature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]