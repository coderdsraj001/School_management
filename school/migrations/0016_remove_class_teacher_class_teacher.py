# Generated by Django 5.0.3 on 2024-04-01 10:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_alter_class_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]