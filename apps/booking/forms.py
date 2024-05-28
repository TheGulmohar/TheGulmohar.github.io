from django import forms

from apps.utils.constants import CHOICES_ROOM_TYPE

class AvailabilityForm(forms.Form):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    room_type = forms.ChoiceField(choices=CHOICES_ROOM_TYPE)
