from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages 

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"El registro fue exitoso.")
            return redirect("split:homepage")
        messages.error(request,"No se pudo registrar, inserte informacion valida")
    form=NewUserForm()
    return render (request=request, template_name="split/register.html", context={"register_form":form})


def homepage(request):
    return render(request,'split/home.html')