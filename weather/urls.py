from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # send variable cityWeather.city
    path('delete/<city>', views.deleteCity, name='deleteCity')
]
