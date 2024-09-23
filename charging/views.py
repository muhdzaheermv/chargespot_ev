from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count

from stationoperator.models import Category,ChargingStation,StationImages,SlotReservation,BookingSlots,StationReview,wishlist,Address,Vendor

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

def category_station_list(request,cid):
    category=Category.objects.get(cid=cid)
    stations=ChargingStation.objects.filter(slot_status="published",category=category)
    
    context={
        "category":category,
        "stations":stations,
    }
    
    return render(request,"category-station_list.html",context)

def vendor_list_view(request):
    vendor = Vendor.objects.all()
    
    context={
        "vendor":vendor,
    }
    return render(request,"vendor-list.html",context)

def vendor_detail_view(request,vid):
    vendor = Vendor.objects.get(vid=vid)
    station = ChargingStation.objects.filter(vendor=vendor,slot_status="published")
    
    context={
        "vendor":vendor,
        "stations":station,
    }
    return render(request,"vendor-detail.html",context)

def station_detail_view(request,csid):
    station = ChargingStation.objects.get(csid=csid)
    
    station_images = station.station_images.all()
    
    context={
        'station':station,
        'station_images':station_images,
    }
    
    return render(request,"station_details_view.html",context)