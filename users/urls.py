from django.urls import path
from . import views
from users.views import index

urlpatterns = [
    path('',index,name='index'),
    path('login/',views.ev_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('register/',views.register,name='register'),
]
