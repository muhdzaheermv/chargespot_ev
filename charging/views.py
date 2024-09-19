from django.http import HttpResponse
from django.shortcuts import render

from stationoperator.models import Category,ChargingStation,StationImages,SlotReservation,BookingSlots,StationReview,wishlist,Address,vendor

def index(request):
    stations =ChargingStation.objects.all()
    
    context = {
        "stations":stations
    }
    
return render(request,'users/index.html',context)