from django.urls import path

from . import views


app_name = 'seasonal_keeping'
urlpatterns = [
    path('', views.display_stuff, name='seasonal-keeping'),
]
