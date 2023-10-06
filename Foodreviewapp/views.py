from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.models import Hotel_list,Rating,Food_Review,Hotel_rating,list
from django.views.decorators.csrf import csrf_exempt
import json
from PIL import Image,ImageDraw
from django.shortcuts import redirect
import re

# Create your views here.
def home(request):
    return render(request,"welcome.html")
    
def register(request):
    return render(request,"register.html")

def regvalidation(request):
    if request.method == 'POST':
        user_name = request.POST["username"]
        user_email = request.POST["email"]
        user_password = request.POST["password"]

        if user_name.isalpha() and user_email.endswith("@gmail.com") and user_password.isdigit() and len(user_password) == 6:
            objUser = User.objects.create_user(username=user_name, email=user_email, password=user_password)
            objUser.save()
            msg="register successfully"
            return render(request, 'register.html',{"msg":msg})
        elif user_password.isdigit() and len(user_password) != 6:
            msg="Enter the password only 6 digit"
            return render(request, 'register.html',{"msg":msg})
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def logins(request):
    return render(request, "log.html")

def logvalidation(request):
    if request.method == 'POST':
        user_email = request.POST["email"]
        user_password = request.POST["password"]
        print(type(user_email))  # Debug statement
        print(type(user_password))  # Debug statement
        global user_name
        user_name=User.objects.filter(email=user_email)
        print(len(user_name))
        print("username",user_name)

        if len(user_name)==1:
            user_name=User.objects.get(email=user_email)
            user = authenticate(username=user_name, password=user_password)
            print(user)
            if user is not None:
                locname=list.objects.all()
                return render(request,"main.html",{"locname":locname})

                    
            if user is None:
                msg=("mismatched") 
                return render(request,"log.html",{"msg":msg})


        else:
            msg="invalid"
            return render(request,"log.html",{"msg":msg})

def hotellocation(request):

    if request.method=="POST":
        global loc_name
        loc_name=request.POST['locname']
        #hotel_name=list.objects.filter(hotel_location=loc_name)
        hotel_name=list.objects.values_list('loc_name').annotate("hotel_location")

        print("A1:",hotel_name)
        locname=list.objects.all()
        print("A2:",locname)
        return render(request,"main.html",{"hotel_name":hotel_name,"locname":locname})

@csrf_exempt
def hotel(request):
    if request.method=='POST':
        data=json.loads(request.body)
        global loc_name
        loc_name=data['l']
        print("data",data)
        hotel_name=list.objects.filter(hotel_location=loc_name)
        locname=list.objects.all()
        return render(request,"hotelname.html",{"hotel_name":hotel_name})
    
@csrf_exempt
def viewss(request):
    if request.method=='POST':
        data=json.loads(request.body)
        global hot_name
        hot_name=data['h']
        print(data['h'])
        main=list.objects.get(hotel_location=loc_name,hotel_name=hot_name)
        print(main)
        thumbnail=main.thumbnail_pic
        print(thumbnail)
        hotelemail=main.hotel_email

        #{% static 'images/level3card.jpg' %}
        return render(request,'viewss.html',{'hotel_name':data['h'],'hotel_location':loc_name,'hotel_email':hotelemail,'thumbnails':thumbnail})

def menus(request):
    
    menus=Rating.objects.filter(hotel_name=hot_name,hotel_location=loc_name)
    print(menus)
    return render(request,'menus.html',{"menus":menus})

def Review(request):
    
    if request.method == 'GET' and 'item' in request.GET:
        global item
        item = request.GET.get('item')
        rv=Food_Review.objects.filter(Items=item,hotel_name=hot_name,hotel_location=loc_name)
        if rv:
            print (rv)
            return render(request,'Review.html',{"rv":rv})
        else:
            msgs="no reviews and ratings yet"
            return render(request,'Review.html',{"msgs":msgs})
    
def gtreview(request):
    
    if request.method=='POST':
            
        ratingoffood=request.POST['rating']
        if int(ratingoffood) <=5:
                
            print(ratingoffood)
            obj1=Food_Review(User_name=user_name,Items=item,hotel_location=loc_name,hotel_name=hot_name,Items_ratings=ratingoffood)
            obj1.save()
            rv=Food_Review.objects.filter(Items=item,hotel_name=hot_name,hotel_location=loc_name)
            msg="review addedd successfully"
            return render(request,'Review.html',{"msg":msg,"rv":rv})
        elif int(ratingoffood)== None:
            rv=Food_Review.objects.filter(Items=item,hotel_name=hot_name,hotel_location=loc_name)
            msg="Yep thank you so much"
            return render(request,'Review.html',{"msg":msg,"rv":rv})
        else:
            rv=Food_Review.objects.filter(Items=item,hotel_name=hot_name,hotel_location=loc_name)
            msg="enter ratings out of 5 only"
            return render(request,'Review.html',{"msg":msg,"rv":rv})
    else:
        return redirect("logins")
    
@csrf_exempt
def check(request):
    if request.method=='POST':
        data=json.loads(request.body)
        print(data)
        if data['card_id']=="bad":
            bad="bad"
            return render(request,"check.html",{"bad":bad})
        elif data['card_id']=="average":
            ratings=2
            obj1=Food_Review(User_name=user_name,Items=item,hotel_location=loc_name,hotel_name=hot_name,Items_review=data['card_id'],Items_ratings=ratings)
            obj1.save()
            msg="Your reviews uploaded"
            return render(request,"check.html",{"msg":msg})

        elif data['card_id']=="good":
            ratings=3
            obj1=Food_Review(User_name=user_name,Items=item,hotel_location=loc_name,hotel_name=hot_name,Items_review=data['card_id'],Items_ratings=ratings)
            obj1.save()
            msg="Your reviews uploaded"
            return render(request,"check.html",{"msg":msg})
        
        elif data['card_id']=="verygood":
            ratings=4
            obj1=Food_Review(User_name=user_name,Items=item,hotel_location=loc_name,hotel_name=hot_name,Items_review=data['card_id'],Items_ratings=ratings)
            obj1.save()
            msg="Your reviews uploaded"
            return render(request,"check.html",{"msg":msg})
        
        elif data['card_id']=="execellent":
            ratings=5
            obj1=Food_Review(User_name=user_name,Items=item,hotel_location=loc_name,hotel_name=hot_name,Items_review=data['card_id'],Items_ratings=ratings)
            obj1.save()
            msg="Your reviews uploaded"
            return render(request,"check.html",{"msg":msg})
def mains(request):
    locname=list.objects.all()
    return render(request,"main.html",{"locname":locname})    
def logouts(request):
    logout(request)
    return redirect("home")

def sad_review(request):
    if request.method=='POST':
        sad=request.POST['rating']
        sad1=request.POST['review']
        obj1=Food_Review(User_name=user_name,Items=item,hotel_location=loc_name,hotel_name=hot_name,Items_review=sad1,Items_ratings=sad)
        obj1.save()
        msg="your reviews uploade successfully"
        return render(request,"Review.html",{"msg":msg})
    
def hotel_rating(request):
    if request.method=='POST':
        rate=request.POST['hotel_rating']
        pattern="[0-5]{1}$"
        match=re.match(pattern,rate)
        
        if match:
            obj1=Hotel_rating(user_name=user_name,hotel_location=hot_name,hotel_name=loc_name,rating=int(rate))
            obj1.save()
            msg="rating uploaded successfully"
            menus=Rating.objects.filter(hotel_name=hot_name,hotel_location=loc_name)
            print(menus)
            print(hot_name)
            print(loc_name)
            obj2=list.objects.filter(hotel_name=hot_name,hotel_location=loc_name)
            print("obj2",obj2)
            for i in obj2:
                print(i)
                print(i.hotel_ratings)
                hotel_rate=i.hotel_ratings
                hotel_rate=hotel_rate+int(rate)
                h_rate=(hotel_rate/2)
                print(h_rate)
                print(type(h_rate))
                obj3=list.objects.get(id=i.id)
                print(obj3)
                hrate=int(h_rate)
                print(type(hrate))
                print(hrate)
                obj3.hotel_ratings=hrate
                obj3.save()
                

            return render(request,'menus.html',{"menus":menus,"msg":msg})
            
        else:
            msg="enter ratings out of 5"
            menus=Rating.objects.filter(hotel_name=hot_name,hotel_location=loc_name)
            print(menus)
            return render(request,'menus.html',{"menus":menus,"msg":msg})
        
            
    
 















  
        
                
                
    