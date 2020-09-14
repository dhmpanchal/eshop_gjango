# Generated by Django 3.1.1 on 2020-09-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
