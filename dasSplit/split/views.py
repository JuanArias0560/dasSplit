from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm

def register_request(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"El registro fue exitoso.")
            return redirect("split:homepage")
        messages.error(request,"No se pudo registrar, inserte informacion valida")
        redirect("split:register")
    form=NewUserForm()
    return render (request=request, template_name="split/register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f'Bienvenido de nuevo {username}')
                return redirect("split:homepage")
            else:
                messages.error(request,"Usuario o contraseña invalidos")
        else:
            messages.error(request,"Usuario o contraseña invalidos")
    form =AuthenticationForm()
    return render(request=request, template_name="split/login.html", context={"login_form":form})
    


def homepage(request):
    return render(request,'split/home.html')