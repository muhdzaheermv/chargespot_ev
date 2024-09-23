from email.policy import default
from pyexpat import model
from unicodedata import decimal
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from users.models import User

STATUS_CHOICE = {
    ("in_process","Booking in Process"),
    ("reserved", "Slot Reserved"),
    ("completed", "Charging Completed"),
}

STATUS = {
    ("draft","Draft"),
    ("disabled","Disabled"),
    ("rejected","Rejected"),
    ("in_review","in Review"),
    ("published","Published"),
}

Rating = {
    (1,"⭐☆☆☆☆"),
    (2,"⭐⭐☆☆☆"),
    (3,"⭐⭐⭐☆☆"),
    (4,"⭐⭐⭐⭐☆"),
    (5,"⭐⭐⭐⭐⭐"),
}

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Category(models.Model):
    cid=ShortUUIDField(unique=True,length=10,max_length=20,prefix="cat",alphabet="abcdef123")
    title=models.CharField(max_length=100,default="CCS2")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Tags(models.Model):
    pass

class Vendor(models.Model):
    vid=ShortUUIDField(unique=True,length=10,max_length=20,prefix="V",alphabet="abcde123")
    title=models.CharField(max_length=100,default="TATA")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    cover_image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    description = models.TextField(null=True,blank=True,default="iam amazinf vendor")


    address=models.CharField(max_length=100,default="123 Main Street london")
    contact=models.CharField(max_length=100,default="1 +91 777 777 777")
    chat_resp_time=models.CharField(max_length=100,default="100")
    charging_efficiency=models.CharField(max_length=100,default="100")
    station_rating=models.CharField(max_length=100,default="100")
    reservation_cancellation_window=models.CharField(max_length=100,default="100")
    maintenance_period=models.CharField(max_length=100,default="100")

    user = models.ForeignKey(User,on_delete=models.SET_NULL ,null=True)
    date = models.DateTimeField(auto_now_add=False,null=True,blank=True)

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class ChargingStation(models.Model):
    csid=ShortUUIDField(unique=True,length=10,max_length=20,alphabet="abcde12")

    user = models.ForeignKey(User,on_delete=models.SET_NULL ,null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL ,null=True,related_name="category")
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL ,null=True,related_name="station")

    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path, default="station.jpg")
    description = models.TextField(null=True,blank=True,default="This is the Charging Station")

    price = models.DecimalField(max_digits=9999999999, decimal_places=2,default="1.99")
    old_price = models.DecimalField(max_digits=9999999999, decimal_places=2,default="2.99")

    specification=models.TextField(null="True",blank="True")
    type=models.CharField(max_length=100,default="CCS2",null="True",blank="True")
    Charging_capacity=models.CharField(max_length=100,default="CCS, >100 kW",null="True",blank="True")
    Charging_time=models.CharField(max_length=100,default="24V",null="True",blank="True")
    installation_date=models.DateField(auto_now_add=False,null="True",blank="True")
    
    # tags=models.ForeignKey(Tags,on_delete=models.SET_NULL ,null=True)

    slot_status=models.CharField(max_length=10,choices=STATUS,default="in_review")

    status=models.BooleanField(default=True)
    in_stock=models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    # digital = models.BooleanField(default=False)

    sku=ShortUUIDField(unique=True,length=4,max_length=10,prefix="CS",alphabet="abcd123")

    date=models.DateField(auto_now_add=True)
    updated=models.DateField(null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Charging Station"

    def station_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price=(self.price/self.old_price) * 100
        return new_price

class StationImages(models.Model):
    images=models.ImageField(upload_to="station-images", default="station.jpg")
    chargingstation = models.ForeignKey(ChargingStation,related_name="station_images",on_delete=models.SET_NULL ,null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Station Images"


        ###########################Cart,Order,OrderItems & address


class SlotReservation(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999, decimal_places=2,default="1.99")
    paid_status=models.BooleanField(default=False)
    booking_date=models.DateField(auto_now_add=True)
    slot_status=models.CharField(max_length=30,choices=STATUS_CHOICE,default="Booking in Process")

    class Meta:
        verbose_name_plural = "slot orders"
        


class BookingSlots(models.Model):
    booking=models.ForeignKey(SlotReservation, on_delete=models.CASCADE)
    invoice_no=models.CharField(max_length=200)
    slot_status=models.CharField(max_length=200)
    item=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    qty=models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999999999, decimal_places=2,default="1.99")
    total = models.DecimalField(max_digits=9999999999, decimal_places=2,default="1.99")

    class Meta:
        verbose_name_plural = "Booking Slots"

    def Booking_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50> />' % {self.image})


#########################################################

class StationReview(models.Model):
        user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
        station=models.ForeignKey(ChargingStation, on_delete=models.SET_NULL,null=True)
        review=models.TextField()
        rating = models.IntegerField(choices=Rating,default=None)
        date = models.DateTimeField(auto_now_add=True)
        

class Meta:
    verbose_name_plural = "Station Reviews"


def __str__(self):
    return self.ChargingStation.title

def get_rating(self):
    return self.rating

###########################################################

class wishlist(models.Model):
        user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
        station=models.ForeignKey(ChargingStation, on_delete=models.SET_NULL,null=True)
        date = models.DateTimeField(auto_now_add=True)
        

class Meta:
    verbose_name_plural = "Station Reviews"


def __str__(self):
    return self.ChargingStation.title

class Address(models.Model):
        user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
        address = models.CharField(max_length=100,null=True)
        status=models.BooleanField(default=False)
        
        class Meta:
            verbose_name_plural = "Address"
    