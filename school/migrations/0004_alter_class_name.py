# Generated by Django 5.0.3 on 2024-04-01 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student_clas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]