# listings/forms.py
from django import forms
from .models import ExersiceSec


#was just Form
class TestExerciseForm(forms.ModelForm):
    class Meta:
        model = ExersiceSec
        fields = ["id", "ex_name", "reps", "weight"]
