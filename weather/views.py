from django.shortcuts import render, redirect
import requests
from .models import Cities
from .form import addCity

# this weather search app is using Open Weather Map API (https://openweathermap.org/api)


def index(response):
    # api url
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0a3bc26ebdd2a2100cbe450afcbce0f9'
    # read all of cities from data base
    cityList = Cities.objects.all()
    # weather informations of every city in database
    citiesWeather = []
    message = ''

    form = addCity()
    if response.method == 'POST':
        form = addCity(response.POST)
        # if form value is valid, sent the value in "name" fields to newCity
        if form.is_valid():
            newCity = form.cleaned_data['cityName']
            # to know is there any duplications with newCity we add (case insensitive)?
            duplicateCity = Cities.objects.filter(
                cityName__iexact=newCity).count()
            if duplicateCity == 0:
                # to know if the city we type in is real in world (corrcet response cod is 200)
                r = requests.get(url.format(newCity)).json()
                if r['cod'] == 200:
                    form.save()
                    message = 'City successfuly added!'
                else:
                    message = 'There is no city called this!'
            else:
                message = 'City is already on the list!'

    # request the data from api with all of city names in database
    for city in cityList:
        r = requests.get(url.format(city)).json()
        cityWeather = {
            'city': city.cityName,
            'temp': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        citiesWeather.append(cityWeather)

    context = {'citiesWeather': citiesWeather, 'form': form,
               'message': message}
    # send context to html
    return render(response, 'weather/weather.html', context)


# recieve variable cityWeather.city
def deleteCity(response, city):
    # if condition of filter is satisfied (case insensitive), delete the coresponding city in database
    deleteCity = Cities.objects.filter(cityName__iexact=city)
    deleteCity.delete()
    return redirect('home')
