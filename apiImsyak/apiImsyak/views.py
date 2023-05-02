from django.shortcuts import render

def index(request):

    context = {
        'title' : 'Selamat berbuka puasa'
    }

    return render(request, 'home.html', context)