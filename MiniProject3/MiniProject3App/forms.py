from django import forms
from .models import Timecard

# class for building new form for teachers timecard
class NewTimecardForm(forms.ModelForm):
    class Meta():
        model = Timecard
        fields = '__all__'
