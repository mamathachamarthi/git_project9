from django.shortcuts import render

# Create your views here.

def third(request):
    d={'name':'SANKAR','age':40}
    return render(request,'first_print.html',context=d)