# Generated by Django 4.2.9 on 2024-01-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placesofvaccination',
            name='vaccination_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
