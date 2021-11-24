from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse

from core.models import (
    Place,
    Storage,
)

from .forms import (
    StorageAddressForm,
    NumberThingsForm,
)
from .models import Thing


def display_stuff(request):
    things = Thing.objects.all()
    ctx = {
        'stuff': things,
    }

    return render(request, 'stuff.html', ctx)


def get_things_count(request):
    if request.method == 'POST':
        number_things_form = NumberThingsForm(request.POST)
        if number_things_form.is_valid():
            url_for_redirect = (request
                                .build_absolute_uri(
                                    reverse('seasonal_keeping:storage-places')
                                ))
            return HttpResponseRedirect(url_for_redirect)
    else:
        number_things_form = NumberThingsForm()

    ctx = {
        'form': number_things_form,
    }
    return render(request, 'things_count.html', ctx)


def get_places(request):
    if request.method == 'POST':
        storage_addresses_form = StorageAddressForm(request.POST)
        if storage_addresses_form.is_valid():
            storage_address = storage_addresses_form.cleaned_data['address']
            place = Place.objects.get(address=storage_address)  # FIXME
            url_for_redirect = (request
                                .build_absolute_uri(
                                    reverse('seasonal_keeping:box-cost',
                                            args=[place.id, ])  # FIXME
                                ))
            return HttpResponseRedirect(url_for_redirect)
    else:
        storage_addresses_form = StorageAddressForm()

    ctx = {
        'form': storage_addresses_form,
    }
    return render(request, 'places.html', ctx)


def display_box_cost(request, storage_id):
    pass
