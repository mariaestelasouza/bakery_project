from django.shortcuts import render

from django.http import HttpResponse
from .models import Bakery, Item


def index(request):
    context = {
        "bakeries": Bakery.objects.all()
    }
    return render(request, "index.html",context)


# Create your views here.
