from django.shortcuts import render, get_object_or_404
from webapp.models import Record


def index_view(request):
    products = Record.objects.filter(status='active').order_by('-created')
    return render(request, 'index.html', context={'products': products})