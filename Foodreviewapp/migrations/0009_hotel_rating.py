# Generated by Django 4.2.1 on 2023-07-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodreviewapp', '0008_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('hotel_location', models.CharField(max_length=50)),
                ('hotel_name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]