from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'bachata/event_list.html', {'events': events})

def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, 'bachata/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'bachata/event_create.html', {'form': form})

def event_edit(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'bachata/event_create.html', {'form': form})


def event_delete (request, pk):
    Event.objects.get(pk=pk).delete()
    return redirect('event_list')