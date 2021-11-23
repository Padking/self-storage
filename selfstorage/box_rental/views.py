from django.shortcuts import render


def display_rental_form(request):
    return render(request, 'box.html')
