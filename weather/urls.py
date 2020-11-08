
from django.urls import path, include
from . import views
from .views import WeatherDeletelView

urlpatterns = [
    path('', views.index, name = "weather-list"),
    path('<int:id>/delete/', WeatherDeletelView.as_view(), name='weather_delete'),
    path('<int:id>/', views.weather_detail_view, name='weather_detail'),
    path('<int:id>/forecast', views.weather_forecast, name='weather_forecast'),





]