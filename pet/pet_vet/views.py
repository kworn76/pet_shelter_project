from django.shortcuts import render


def index(request):
    return render(request, 'pet_vet/index.html')
