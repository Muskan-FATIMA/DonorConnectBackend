# Generated by Django 5.0.4 on 2024-05-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='donor',
            field=models.CharField(max_length=50),
        ),
    ]
