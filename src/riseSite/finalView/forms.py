from django.forms import ModelForm
from finalView.models import Event

class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        exclude = []