from stationoperator.models import Category,ChargingStation,StationImages,SlotReservation,BookingSlots,StationReview,wishlist,Address,Vendor

def default(request):
    categories = Category.objects.all()
    
    return {
        'categories':categories,
    }