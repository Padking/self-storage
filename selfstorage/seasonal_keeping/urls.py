from django.urls import path

from . import views


app_name = 'seasonal_keeping'
urlpatterns = [
    path('', views.get_thing_name, name='seasonal-keeping'),
    path('count-of-things/', views.get_things_count, name='things-count'),
    path('places/', views.get_places, name='storage-places'),
    path('places/storage/<int:storage_id>/box-cost/', views.display_box_cost, name='box-cost'),
    path('places/storage/<int:storage_id>/storage-period/', views.get_storage_period, name='storage-period')
]
