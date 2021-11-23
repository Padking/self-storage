from django.urls import path

from . import views


app_name = 'box_rental'
urlpatterns = [
    path('', views.display_rental_form, name='box-rental'),
]
