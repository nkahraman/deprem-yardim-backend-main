# Generated by Django 4.1.6 on 2023-02-07 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_entry_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formatted_address', models.TextField(blank=True, null=True)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('northeast_lat', models.FloatField(default=0.0)),
                ('northeast_lng', models.FloatField(default=0.0)),
                ('southwest_lat', models.FloatField(default=0.0)),
                ('southwest_lng', models.FloatField(default=0.0)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.entry')),
            ],
        ),
    ]
