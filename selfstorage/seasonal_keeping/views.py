from django.shortcuts import render


def display_stuff(request):
    return render(request, 'stuff.html')
