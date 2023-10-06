from django.db import models
from django.contrib.auth.models import User
from PIL import Image,ImageDraw
import pickle 
# Create your models here.
class Hotel_list(models.Model):
    inf_hotel=models.CharField(max_length=220)
    hotel_location=models.CharField(max_length=220)
    hotel_name=models.CharField(max_length=220)
    hotel_email=models.EmailField()
    thumbnail_pic=models.BinaryField()
    hotel_review=models.CharField(max_length=520)
    hotel_ratings=models.IntegerField()
    
class list(models.Model):
    inf_hotel=models.CharField(max_length=220)
    hotel_location=models.CharField(max_length=220)
    hotel_name=models.CharField(max_length=220)
    hotel_email=models.EmailField()
    hotel_ratings=models.IntegerField()
    thumbnail_pic=models.CharField(max_length=220)
class Rating(models.Model):
    Items=models.CharField(max_length=220)
    rate=models.DecimalField(max_digits=10,decimal_places=3)
    hotel_location=models.CharField(max_length=220)
    hotel_name=models.CharField(max_length=220)
    Items_review=models.CharField(max_length=520)
    Items_ratings=models.IntegerField()
    hotel_review=models.CharField(max_length=520)
    hotel_ratings=models.IntegerField()

"""class Review(models.Model):
    User_name=models.CharField(max_length=220)
    Items=models.CharField(max_length=220)
    hotel_location=models.CharField(max_length=220)
    hotel_name=models.CharField(max_length=220)
    Items_review=models.CharField(max_length=520,default='0',editable=True)
    Items_ratings=models.IntegerField(default='0',editable=True)"""

class Food_Review(models.Model):
    User_name=models.CharField(max_length=220)
    Items=models.CharField(max_length=220)
    hotel_location=models.CharField(max_length=220)
    hotel_name=models.CharField(max_length=220)
    Items_review=models.CharField(max_length=520,default='0',editable=True)
    Items_ratings=models.IntegerField(default='0',editable=True)
    
class Hotel_rating(models.Model):
    user_name=models.CharField(max_length=50)
    hotel_location=models.CharField(max_length=50)
    hotel_name=models.CharField(max_length=50)
    rating=models.IntegerField()



