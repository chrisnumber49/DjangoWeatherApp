# Django Weather App

An weather application that built with Django, Bootstrap, python, CSS and the Open Weather Map API

This application is deployed on: https://djangoweatherappchris49.herokuapp.com/

Open Weather Map API: https://openweathermap.org/api

## Project Screen Shots
<img src="https://github.com/chrisnumber49/DjangoWeatherApp/blob/master/screen%20shot/demo1.PNG" width="600" > 
<img src="https://github.com/chrisnumber49/DjangoWeatherApp/blob/master/screen%20shot/demo2.PNG" width="600" > 

## Installation and Setup Instructions

Clone down this repository. You will need `django` installed globally on your machine.  

Installation: `pip install Django`

Creating new migrations: `python manage.py makemigrations`

Applying migrations: `python manage.py migrate`

To Start Server: `python manage.py runserver`  

To Visit App: `localhost:8000/`

## Reflection 

This is my first side project of learning Django. In this project we can query the weather with the specific city name we type in, then store the city into database if the response from Open Weather Map API is correct. I started this project by using the command `django-admin startproject` to create the boilerplate of project, then create new app with command `python manage.py startapp`.

At the end through this side project, I learned about the basic concept of MVT (Model-View-Template) architecture in django to know how...
