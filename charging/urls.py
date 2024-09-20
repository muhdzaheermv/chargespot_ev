from django.urls import path
from charging import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('category/',views.category_list_view,name='category-list'),
    path('station/',views.stations_list_view,name='stations-list'),
    path('category/<cid>/',views.category_station_list__view,name='category-station-list'),
]
