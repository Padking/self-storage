from django.shortcuts import render
from django.contrib.auth.models import User

from box.models import BoxOrder
from box.forms import BoxOrderForm


def create_box_order(request):
    if request.method == 'POST':
        box_order_form = BoxOrderForm(request.POST)
        if box_order_form.is_valid():
            # BoxOrder.objects.create(
            #     id=1000,
            #     box=box_order_form.cleaned_data['box'],
            #     rent_term=box_order_form.cleaned_data['rent_term'],
            #     tenant=box_order_form.cleaned_data['tenant']
            # )
            return render(request, 'success_order.html')
    else:
        box_order_form = BoxOrderForm()

    context = {
        'form': box_order_form,
    }

    return render(request, 'index.html', context)
