from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse

from .forms import NumberThingsForm
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
    url_for_redirect = request.build_absolute_uri(reverse('seasonal_keeping:box-cost',
                                                          args=[1, ]))
    return HttpResponseRedirect(url_for_redirect)


def display_box_cost(request, place_id):
    return HttpResponse('Здесь будут стоимости хранения')
