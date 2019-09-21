from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import RecordForm
from webapp.models import Record


def index_view(request):
    records = Record.objects.filter(status='active').order_by('-created')
    return render(request, 'index.html', context={'records': records})


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


def update_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'GET':
        form = RecordForm(data={
            'name': record.name,
            'mail': record.email,
            'text': record.text,
        })
        return render(request, 'update.html', context={'form': form, 'record': record})
    elif request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record.name = form.cleaned_data['name']
            record.email = form.cleaned_data['mail']
            record.text = form.cleaned_data['text']
            record.save()
            return redirect('index_view', pk=record.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'record': record})