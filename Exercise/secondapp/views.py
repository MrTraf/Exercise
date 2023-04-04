from django.http import HttpResponseRedirect #new maybe have to kill
from django.shortcuts import render,redirect
from secondapp.forms import TestExerciseForm
from secondapp.models import exersice_sec
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
exercise = [
  { 'exercise_name' : 'squats','repeat':'10', 'weight' : '60'},
  { 'exercise_name' : 'wallball','repeat': '12', 'weight' : '10'},
  { 'exercise_name' : 'pull ups','repeat': '7', 'weight' : '0'},
  { 'exercise_name' : 'overheads','repeat': '5', 'weight' : '40'},
  { 'exercise_name' : 'wheel','repeat': '4', 'weight' : '0'},
  { 'exercise_name' : 'thruster','repeat': '1', 'weight' : '50'},
  { 'exercise_name' : 'snatch','repeat': '1', 'weight' : '53'}

]





def home(request):
 # The context is all of the variables we want passed into the template.
  context = {"exercise" : exercise}
  return render(request, 'secondapp/home.html', context)

def input(request):
 # The context is all of the variables we want passed into the template.
 #it was here form = TestExerciseForm() 
#from here new line  "kill"
    if request.method == 'POST':
       # create a form instance and populate it with data from the request:
       form = TestExerciseForm(request.POST)
       # check whether it's valid:
       if form.is_valid():
          # process the data in form.cleaned_data as required
          # ...
          # redirect to a new URL:
          return HttpResponseRedirect('display/')
    # if a GET (or any other method) we'll create a blank form
    else:
         form = TestExerciseForm() 
#to here new line  "kill"

#23.03.2023
#from secondapp.forms import TestExerciseForm
#def home(request):
# form = TestExerciseForm() #instantiate a new form here
 # return render(request,
  #        'secondapp/home.html',
   #       {'form': form}) # pass that form to the template

#new one
###def second_input(request):
## form =TestExerciseForm(request.POST or None)
## if form.is_valid():
##    form.save()
## context1={'form': form}  
## return render(request, 'secondapp/second_input.html', context1)
#second_new_one
#from .models import exersice_sec
###    return render(request,'second_input.html',{'msg':'Data insert'})
#
def Insertrecord(request): #change it! use slack
 if request.method=='POST':
    if request.POST.get('ex_name') and request.POST.get('reps') and request.POST.get('weight'):
       saverecord=exersice_sec()
       saverecord.ex_name=request.POST.get('ex_name')
       saverecord.reps=request.POST.get('reps')
       saverecord.weight=request.POST.get('weight')
       saverecord.save()
       messages.success(request,'Record Saved')
       return render(request,'secondapp/second_input.html')
 else:
       return render(request,'secondapp/second_input.html') 
def display(request):
	st=exersice_sec.objects.all() # Collect all records from table 
	return render(request,'secondapp/display.html', {'st':st})
