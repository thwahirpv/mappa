from django.urls import include, path
from .views import *



app_name = 'account'

urlpatterns = [
    path('home/', home, name='user_home'),
    path('register/', registration, name='registration'),
    path('login/', login, name='login'), 
    path('logout/', logout, name='logout'),
]