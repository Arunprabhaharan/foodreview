from django.contrib import admin
from .models import list,Food_Review,Hotel_rating,Rating

@admin.register(list)
class list(admin.ModelAdmin):
    list_display = ("id", 'hotel_name','hotel_ratings',"hotel_location")
    list_filter = ('hotel_name','hotel_ratings',"hotel_location")
    search_fields=["id",'hotel_name','hotel_ratings',"hotel_location"]
    """def has_delete_permission(self, request):
        # Disable delete
        return True
    def has_add_permission(self,request):
        return True"""

@admin.register(Food_Review)
class Food_Review(admin.ModelAdmin):
    list_display = ("User_name","Items",'hotel_name',"hotel_location","Items_review","Items_ratings")
    list_filter = ("User_name","Items",'hotel_name',"hotel_location","Items_review","Items_ratings")
    search_fields=["User_name","Items",'hotel_name',"hotel_location","Items_review","Items_ratings"]

@admin.register(Rating)
class Rating(admin.ModelAdmin):
    list_display = ("Items","rate", 'hotel_name','hotel_ratings',"hotel_location","Items_review","Items_ratings")
    list_filter = ("Items","rate", 'hotel_name','hotel_ratings',"hotel_location","Items_review","Items_ratings",)
    search_fields=["Items","rate", 'hotel_name','hotel_ratings',"hotel_location","Items_review","Items_ratings",]

@admin.register(Hotel_rating)
class Hotel_rating(admin.ModelAdmin):
    list_display = ("user_name", 'hotel_name',"hotel_location","rating",)
    list_filter = ('hotel_name','rating',"hotel_location")
    search_fields=['hotel_name','rating',"hotel_location"]


