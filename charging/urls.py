from django.urls import path
from charging import views

urlpatterns = [
    # Homepage
    path('index',views.index,name='index'),
    path('category/',views.category_list_view,name='category-list'),
    path('station/<csid>/',views.station_detail_view,name='stations-detail'),

    # Category
    path('station/',views.stations_list_view,name='stations-list'),
    path('category/<cid>/',views.category_station_list,name='category-station-list'),

    # Vendor
    path('vendor/',views.vendor_list_view,name='vendor-list'),
    path('vendor/<vid>/',views.vendor_detail_view,name='vendor-detail'),
    
]
