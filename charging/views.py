from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Count,Avg
from taggit.models import Tag

from stationoperator.models import Category,ChargingStation,StationImages,SlotReservation,BookingSlots,StationReview,wishlist,Address,Vendor


# HomePage

def index(request):
    
    stations = ChargingStation.objects.filter(slot_status="published",featured="True")
    
    context={
        "stations":stations
    }
    return render(request,'index.html',context)

# Category List

def category_list_view(request):
    
    categories = Category.objects.all().annotate(product_count=Count("category"))
    
    context={
        "categories":categories
    }
    
    return render(request,'category_list.html',context)

# Stations List

def stations_list_view(request):
    
    stations = ChargingStation.objects.filter(slot_status="published",featured="True")
    
    context={
        "stations":stations
    }
    return render(request,'station_list.html',context)

# Station list View

def category_station_list(request,cid):
    category=Category.objects.get(cid=cid)
    stations=ChargingStation.objects.filter(slot_status="published",category=category)
    
    context={
        "category":category,
        "stations":stations,
    }
    
    return render(request,"category-station_list.html",context)

# Vendor List View

def vendor_list_view(request):
    vendor = Vendor.objects.all()
    
    context={
        "vendor":vendor,
    }
    return render(request,"vendor-list.html",context)

# Vendor Detail View

def vendor_detail_view(request,vid):
    vendor = Vendor.objects.get(vid=vid)
    station = ChargingStation.objects.filter(vendor=vendor,slot_status="published")
    
    context={
        "vendor":vendor,
        "stations":station,
    }
    return render(request,"vendor-detail.html",context)

# Station Detail View

def station_detail_view(request,csid):
    station = ChargingStation.objects.get(csid=csid)
    stations = ChargingStation.objects.filter(category=station.category).exclude(csid=csid)
    
    reviews=StationReview.objects.filter(station=station).order_by("-date")
    
    average_rating = StationReview.objects.filter(station=station).aggregate(rating=Avg('rating'))
    
    station_images = station.station_images.all()
    
    context={
        'station':station,
        'station_images':station_images,
        'average_rating':average_rating,
        'reviews':reviews,
        'stations':stations,
    }
    
    return render(request,"station_details_view.html",context)

def tag_list(request, tag_slug=None):

    station = ChargingStation.objects.filter(slot_status="published").order_by("-id")

    tag = None 
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        stations = station.filter(tags__in=[tag])

    context = {
        "stations": stations,
        "tag": tag
    }

    return render(request, "tag.html", context)