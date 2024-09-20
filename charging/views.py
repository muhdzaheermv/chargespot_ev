from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count

from stationoperator.models import Category,ChargingStation,StationImages,SlotReservation,BookingSlots,StationReview,wishlist,Address,vendor

def index(request):
    
    stations = ChargingStation.objects.filter(slot_status="published",featured="True")
    
    context={
        "stations":stations
    }
    return render(request,'index.html',context)

def category_list_view(request):
    
    categories = Category.objects.all().annotate(product_count=Count("category"))
    
    context={
        "categories":categories
    }
    
    return render(request,'category_list.html',context)

def stations_list_view(request):
    
    stations = ChargingStation.objects.filter(slot_status="published",featured="True")
    
    context={
        "stations":stations
    }
    return render(request,'station_list.html',context)