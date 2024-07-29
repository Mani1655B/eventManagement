# Generated by Django 5.0.7 on 2024-07-22 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='authentication.event'),
        ),
    ]
