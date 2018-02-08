# Generated by Django 2.0.2 on 2018-02-01 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('country_abbreviation', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
            ],
        ),
    ]
