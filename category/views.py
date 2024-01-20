from django.shortcuts import render,redirect
from . import forms

# Create your views here.

def category(request):
    if request.method == 'POST':
        category_form = forms.CatForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect ('cat')
    
    else :
        category_form = forms.CatForm()

    return render(request,'cat.html',{'form' : category_form })