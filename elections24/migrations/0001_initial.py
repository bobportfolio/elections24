# Generated by Django 4.2.8 on 2024-02-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('gss_code', models.CharField(max_length=15)),
                ('three_code', models.CharField(max_length=4)),
                ('region', models.CharField(max_length=255)),
                ('electorate', models.PositiveIntegerField()),
            ],
        ),
    ]
