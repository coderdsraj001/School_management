# Generated by Django 5.0.3 on 2024-04-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_alter_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
