from django import forms
from django.forms import widgets
from .models import Event

class EventForm(forms.ModelForm):
    time_start = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p'))
    time_end = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p'))
    class Meta:
        model = Event
        fields = ('name', 'date', 'time_start', 'time_end', 'location', 'details', 'cost', 'event_site')
        