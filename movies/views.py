from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'movies': ['matrix', 'top gun', 'casino']
    }
    return render(request, 'movies/index.html', context)


def about(request):
    return render(request, 'movies/about.html', {})