# Generated by Django 4.1.6 on 2023-02-06 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_alter_location_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='formatted_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
