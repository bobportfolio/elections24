from django.shortcuts import render


def index(request):
    args = {'page': 'Home'}
    return render(request, 'elections24/index.html', args)
