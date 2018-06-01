from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


from django.contrib.auth import login, authenticate
from .forms import EventForm
from .models import Event

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'bachata/event_list.html', {'events': events})



@login_required
def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, 'bachata/event_detail.html', {'event': event})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'bachata/event_create.html', {'form': form})

@login_required
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

@login_required
def event_delete (request, pk):
    Event.objects.get(pk=pk).delete()
    return redirect('event_list')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'bachata/signup.html'
