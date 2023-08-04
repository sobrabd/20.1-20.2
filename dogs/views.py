from django.shortcuts import render
from .models import Category


# Create your views here.
def index(request):
    context = {
        'objects_list': Category.objects.all(),
        'title': 'Питомник - Наши породы'
    }

    return render(request, 'dogs/base.html', context)

