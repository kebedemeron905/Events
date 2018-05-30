from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date', 'time_start', 'time_end', 'location', 'details', 'cost', 'event_site')