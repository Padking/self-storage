from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse

from ..models import (
    Place,
    Thing
)

from ..forms import (
    NumberThingsForm,
    StorageAddressForm,
)


def get_thing_name(request):
    if request.method == 'POST':
        things_names = request.POST.getlist('things_names')
        # Сохранить выбор П-ля (название вещи)
        url_for_redirect = (request
                            .build_absolute_uri(
                                reverse('things-count')
                            ))
        return HttpResponseRedirect(url_for_redirect)
    else:
        things = Thing.objects.all()

    ctx = {
        'stuff': things,
    }

    return render(request, 'stuff.html', ctx)


def get_things_count(request):
    if request.method == 'POST':
        number_things_form = NumberThingsForm(request.POST)
        if number_things_form.is_valid():
            number_of_things = number_things_form.cleaned_data['number_of_things']
            # Сохранить выбор П-ля (кол-во единиц вещей)
            url_for_redirect = (request
                                .build_absolute_uri(
                                    reverse('storage-places')
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
            # Сохранить выбор П-ля (адрес склада)
            place = Place.objects.get(address=storage_address)  # FIXME
            url_for_redirect = (request
                                .build_absolute_uri(
                                    reverse('box-cost',
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
    if request.method == 'POST':  # нажата кнопка "Далее"
        place = Place.objects.get(id=storage_id)
        url_for_redirect = (request
                            .build_absolute_uri(
                                reverse('storage-period',
                                        args=[place.id, ])  # FIXME
                            ))
        return HttpResponseRedirect(url_for_redirect)
    else:
        pass

    ctx = {
        # 'form': ,
    }

    return render(request, 'box_cost.html', ctx)


def get_storage_period(request, storage_id):
    if request.method == 'POST':
        # Сохранить выбор П-ля (период хранения конкретной вещи)
        pass
    else:
        return render(request, 'storage_period.html')
