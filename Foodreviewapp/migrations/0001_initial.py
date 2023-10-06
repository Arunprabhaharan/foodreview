# Generated by Django 4.2.1 on 2023-06-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotellist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inf_hotel', models.CharField(max_length=220)),
                ('hotel_location', models.CharField(max_length=220)),
                ('hotel_name', models.CharField(max_length=220)),
                ('hotel_email', models.EmailField(max_length=254)),
                ('thumbnail_pic', models.BinaryField()),
            ],
        ),
    ]
