from django.shortcuts import render, redirect
from .My_form import MyForm
 
 
def index(request):
    if request.method == "GET":
        obj = MyForm()
        return render(request, 'index.html', {'form': obj})
    elif request.method == "POST":
        obj = MyForm(request.POST, request.FILES)
        if obj.is_valid():
            values = obj.clean()
            print(values)
        else:
            errors = obj.errors
            print(errors)
        return render(request, 'index.html', {'form': obj})
    else:
        return redirect('http://www.google.com')