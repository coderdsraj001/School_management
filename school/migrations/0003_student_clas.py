# Generated by Django 5.0.3 on 2024-03-29 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='clas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.class'),
        ),
    ]
