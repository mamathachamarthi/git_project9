from django.shortcuts import render

# Create your views here.

def second(request):
    d={'name':'CHANDU','age':35}
    return render(request,'first_print.html',context=d)