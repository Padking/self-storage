from django.contrib.auth.models import User
from django.core.management.utils import get_random_secret_key as get_random_password
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse

from random_username.generate import generate_username

from box.models import (
    Storage,
    SeasonalKeepingOrder,
    Thing,
)

from box.forms import (
    NumberThingsForm,
    StorageAddressForm,
)


def get_thing_name(request):
    if request.method == 'POST':
        things_names = request.POST.getlist('things_names')
        username = request.session.get('username')
        user, _ = User.objects.get_or_create(username=username,
                                             defaults={
                                                 'password': get_random_password()
                                             })
        things_names_for_db_column = ','.join(things_names)
        new_order = (SeasonalKeepingOrder.objects
                     .create(things_names=things_names_for_db_column, tenant=user))

        user.orders.add(new_order)
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
    random_username_for_anonymous = generate_username()[0]
    request.session.setdefault('username', random_username_for_anonymous)

    return render(request, 'stuff.html', ctx)


def get_things_count(request):
    if request.method == 'POST':
        number_things_form = NumberThingsForm(request.POST)
        if number_things_form.is_valid():
            number_of_things = number_things_form.cleaned_data['number_of_things']
            username = request.session.get('username')
            user = User.objects.get(username=username)
            # Взять последний заказ (потенциальный) П-ля
            current_order = user.orders.last()
            current_order.number_of_things = number_of_things
            current_order.save()
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
            username = request.session.get('username')
            user = User.objects.get(username=username)
            current_order = user.orders.last()
            current_order.storage_address = storage_address
            current_order.save()
            place = Storage.objects.get(address=storage_address)  # FIXME
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
        place = Storage.objects.get(id=storage_id)
        url_for_redirect = (request
                            .build_absolute_uri(
                                reverse('storage-period',
                                        args=[place.id, ])  # FIXME
                            ))
        return HttpResponseRedirect(url_for_redirect)
    else:
        username = request.session.get('username')
        user = User.objects.get(username=username)
        current_order = user.orders.last()
        things_names = current_order.things_names.split(',')
        selected_tenant_things = Thing.objects.filter(name__in=things_names)

        costs = {}
        for thing_name in things_names:
            costs_ = selected_tenant_things.get_seasonal_keeping_costs(thing_name)
            costs.update({thing_name: costs_})

    ctx = {
        'things_map_costs': costs,
    }

    return render(request, 'box_cost.html', ctx)


def get_storage_period(request, storage_id):
    if request.method == 'POST':
        # Сохранить выбор П-ля (период хранения конкретной вещи)
        pass
    else:
        return render(request, 'storage_period.html')
