# Generated by Django 4.2.8 on 2024-02-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections24', '0002_postcode'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='postcode',
            index=models.Index(fields=['postcode'], name='elections24_postcod_d2e1a3_idx'),
        ),
    ]
