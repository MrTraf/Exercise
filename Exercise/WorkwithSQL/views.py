from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second_input(request):
    return render(request,'WorkwithSQL/test.html')
#    return HttpResponse("Hey it should work!")
