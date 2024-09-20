from django.urls import path
from users import views

urlpatterns = [
    path('',views.home,name='home'),
    path('stations/',views.stations_list_view,name='stations-list'),
    path('category/',views.category_list_view,name='category-list'),
    path('index',views.index,name='index'),
    path('index',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register'),
]
