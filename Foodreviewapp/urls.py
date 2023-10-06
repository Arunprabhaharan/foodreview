from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),
    path("register",views.register,name="register"),
    path("regvalidation",views.regvalidation,name="regvalidation"),
    path("logins",views.logins,name="logins"),
    path("logvalidation",views.logvalidation,name="logvalidation"),
    path("hotellocation",views.hotellocation,name="hotellocation"),
    path("viewss",views.viewss,name="viewss"),
    path("hotel",views.hotel,name="hotel"),
    path("menus",views.menus,name="menus"),
    path("Review",views.Review,name="Review"),
    path('gtreview',views.gtreview,name="gtreview"),
    path("mains",views.mains,name="mains"),
    path("logouts",views.logouts,name="logouts"),
    path("check",views.check,name="check"),
    path('sad_review',views.sad_review,name='sad_review'),
    path('hotel_rating',views.hotel_rating,name='hotel_rating'),
]