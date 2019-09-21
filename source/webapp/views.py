from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import RecordForm
from webapp.models import Record


def index_view(request):
    products = Record.objects.filter(status='active').order_by('-created')
    return render(request, 'index.html', context={'products': products})

def create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = RecordForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():

            Record.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['mail'],
                text=form.cleaned_data['text'])
            return redirect('index')
        else:


            return render(request, 'create.html', context={'form': form})
