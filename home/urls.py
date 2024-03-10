from django.urls import include, path
from .views import *

app_name = 'home'

urlpatterns = [
    path('complant/', raise_complant, name='complant'),
]