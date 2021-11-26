"""selfstorage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from box.views import (
    main_page,
    box_rental,
    seasonal_keeping,
)


box_rental_extra_patterns = [
    path('', box_rental.display_rental_form, name='box-rental'),
]

seasonal_keeping_extra_patterns = [
    path('', seasonal_keeping.get_thing_name, name='seasonal-keeping'),
    path('count-of-things/', seasonal_keeping.get_things_count, name='things-count'),
    path('places/', seasonal_keeping.get_places, name='storage-places'),
    path('places/storage/<int:storage_id>/box-cost/',
         seasonal_keeping.display_box_cost, name='box-cost'),

    path('places/storage/<int:storage_id>/storage-period/',
         seasonal_keeping.get_storage_period, name='storage-period')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page.index),
    path('box-rental/', include(box_rental_extra_patterns)),
    path('seasonal-keeping/', include(seasonal_keeping_extra_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
