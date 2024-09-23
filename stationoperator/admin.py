from django.contrib import admin
from . models import Category,ChargingStation,StationImages,SlotReservation,BookingSlots,StationReview,wishlist,Address,Vendor

class StationImagesAdmin(admin.TabularInline):
    model = StationImages
    
class ChargingStationAdmin(admin.ModelAdmin):
    inlines=[StationImagesAdmin]
    list_display=['user','title','station_image','price','category','vendor','featured','slot_status','csid']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','category_image']
    
class VendorAdmin(admin.ModelAdmin):
    list_display=['title','vendor_image']
    
class SlotReservationAdmin(admin.ModelAdmin):
    list_display=['user','price','paid_status','booking_date','slot_status']

class BookinSlotAdmin(admin.ModelAdmin):
    list_display=['booking','invoice_no','slot_status','item','image','qty','price','total']
    
class StationReviewAdmin(admin.ModelAdmin):
    list_display=['user','station','review','rating','date']
    
class WishlistAdmin(admin.ModelAdmin):
    list_display=['user','station','date']
    
class AddressAdmin(admin.ModelAdmin):
    list_display=['user','address','status']
    
admin.site.register(ChargingStation,ChargingStationAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(SlotReservation,SlotReservationAdmin)
admin.site.register(BookingSlots,BookinSlotAdmin)
admin.site.register(StationReview,StationReviewAdmin)
admin.site.register(wishlist,WishlistAdmin)
admin.site.register(Address,AddressAdmin)
