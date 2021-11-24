from django.urls import path

from . import views


app_name = 'seasonal_keeping'
urlpatterns = [
    path('', views.display_stuff, name='seasonal-keeping'),
    path('count-of-things/', views.get_things_count, name='things-count'),
    path('places/', views.get_places, name='storage-places'),
    path('places/storage/<int:storage_id>/box-cost/', views.display_box_cost, name='box-cost'),
]
