# listings/forms.py

#from django import forms
#class TestExerciseForm(forms.Form):
#   Exercise_name = forms.CharField(required=False)
#   Exercise_reps = forms.CharField(required=False, max_length=100)
#   Weight = forms.CharField(max_length=1000)
from django import forms
from .models import exersice_sec

class TestExerciseForm(forms.ModelForm): #was just Form
 class Meta:
   model = exersice_sec
#   Exercise_name = forms.CharField(required=False)
#  Exercise_reps = forms.CharField(required=False, max_length=100)
#   Weight = forms.CharField(max_length=1000)
   fields=["id","ex_name","reps","weight"]
