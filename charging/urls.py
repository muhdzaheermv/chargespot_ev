from django.urls import path
from charging import views

urlpatterns = [
    # Homepage
    path('index',views.index,name='index'),
    path('category/',views.category_list_view,name='category-list'),

    # Category
    path('station/',views.stations_list_view,name='stations-list'),
    path('category/<cid>/',views.category_station_list__view,name='category-station-list'),

    # Vendor
    path('vendor/',views.vendor_list_view,name='vendor-list'),
    
]
