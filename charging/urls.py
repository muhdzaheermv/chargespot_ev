from django.urls import path
from charging import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('category/',views.category_list_view,name='category-list'),
    path('stations/',views.stations_list_view,name='stations-list'),
]
