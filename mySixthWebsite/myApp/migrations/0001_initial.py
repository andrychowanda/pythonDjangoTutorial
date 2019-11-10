# Generated by Django 2.2.7 on 2019-11-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('phoneNumber', models.IntegerField()),
            ],
        ),
    ]
