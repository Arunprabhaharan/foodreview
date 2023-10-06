# Generated by Django 4.2.1 on 2023-07-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodreviewapp', '0006_food_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=220)),
                ('Items', models.CharField(max_length=220)),
                ('hotel_location', models.CharField(max_length=220)),
                ('hotel_name', models.CharField(max_length=220)),
                ('Items_review', models.CharField(default='0', max_length=520)),
                ('Items_ratings', models.IntegerField(default='0')),
            ],
        ),
    ]