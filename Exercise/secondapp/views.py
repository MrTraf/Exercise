from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from secondapp.forms import TestExerciseForm
from secondapp.models import ExersiceSec
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
exercise = [
    {'exercise_name': 'squats', 'repeat': '10', 'weight': '60'},
    {'exercise_name': 'wallball', 'repeat': '12', 'weight': '10'},
    {'exercise_name': 'pull ups', 'repeat': '7', 'weight': '0'},
    {'exercise_name': 'overheads', 'repeat': '5', 'weight': '40'},
    {'exercise_name': 'wheel', 'repeat': '4', 'weight': '0'},
    {'exercise_name': 'thruster', 'repeat': '1', 'weight': '50'},
    {'exercise_name': 'snatch', 'repeat': '1', 'weight': '53'}
]


def home(request):
    # Collect all records from table
    st = ExersiceSec.objects.all()
    return render(request, 'secondapp/display.html', {'st': st})


def input(request):
    # The context is all of the variables we want passed into the template.
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestExerciseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # redirect to a new URL:
            return HttpResponseRedirect('display/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestExerciseForm()


def Insert_record(request):
    if request.method == 'POST':
        if request.POST.get('ex_name') and request.POST.get('reps') and request.POST.get('weight'):
            saverecord = ExersiceSec()
            saverecord.ex_name = request.POST.get('ex_name')
            saverecord.reps = request.POST.get('reps')
            saverecord.weight = request.POST.get('weight')
            saverecord.save()
            messages.success(request, 'Record Saved')
        return render(request, 'secondapp/second_input.html')
    else:
        return render(request, 'secondapp/second_input.html')


def display(request):
    # Collect all records from table
    st = ExersiceSec.objects.all()
    return render(request, 'secondapp/display.html', {'st': st})
