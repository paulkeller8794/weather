
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import requests
from .models import City
from .form import CityForm
from django.views.generic import (
    DeleteView,
)


# Create your views here.

def data(request):
    url = url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=99f8110d8e1d8685cbefb01dc1a8fb5e'
    #if request.method == 'POST':
    form = CityForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        temperat = r['main']['temp']
        tt = round(temperat)
        city_weather = {
            'city': city.name,
            'temperature': tt,
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'id': city.id,
            'instance': city,

        }
        weather_data.append(city_weather)
    print(weather_data)
    queryset = City.objects.all()  # list of objects
    context = {'weather_data': weather_data, 'form': form, 'object_list': queryset}
    return context


def index(request):
    context = data(request)
    return render(request, "weather/weather.html", context)


class WeatherDeletelView(DeleteView):
    template_name = 'weather/weather_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(City, id=id_)

    def get_success_url(self):
        return reverse("weather-list")


def weather_detail_view(request, id):
    obj = City.objects.get(id=id)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=99f8110d8e1d8685cbefb01dc1a8fb5e'
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        temperat = r['main']['temp']
        tt = round(temperat)
        city_weather = {
            'city': city.name,
            'temperature': tt,
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'id': city.id
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'object': obj, 'counter': 0 }
    return render(request, "weather/weather_detail.html", context)


def weather_forecast(request, id):
    obj = City.objects.get(id=id)
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&cnt=3&appid=f433793f8d9a04bf07a16813d323a1df'
    cities = City.objects.all()
    forecast_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        for i in range(3):
            city_weather = {
                'city': city.name,
                'temperature': r['list'][i]['main']['temp'],
                'description': r['list'][i]['weather'][0]['description'],
                'icon': r['list'][i]['weather'][0]['icon'],
                'id': city.id,
                'date': r['list'][i]['dt_txt']
            }
            forecast_data.append(city_weather)

    context = {'weather_data': forecast_data, 'object': obj, }
    return render(request, "weather/weather_forecast.html", context)


