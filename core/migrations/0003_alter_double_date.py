# Generated by Django 4.0.5 on 2022-07-02 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_double_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='double',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 7, 2, 14, 17, 55, 179698), null=True),
        ),
    ]
