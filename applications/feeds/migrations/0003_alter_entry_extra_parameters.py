# Generated by Django 4.1.6 on 2023-02-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_alter_entry_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='extra_parameters',
            field=models.TextField(blank=True, null=True),
        ),
    ]
