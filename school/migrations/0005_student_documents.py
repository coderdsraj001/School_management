# Generated by Django 5.0.3 on 2024-04-01 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_class_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='school/documents/'),
        ),
    ]
