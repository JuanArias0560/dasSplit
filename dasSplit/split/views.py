from django.shortcuts import render,redirect, get_object_or_404

from .forms import ChargeForm, PocketForm, NewUserForm,PaymentForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User



def register_request(request):

    if request.user.is_authenticated:
        return redirect("split:homepage")

    else:

        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)
                messages.success(request,"Registration was successful.")
                return redirect("split:feed")
            messages.error(request,"It was not possible to regisster, please insert valid information")
            redirect("split:register")
        form=NewUserForm()
        return render (request=request, template_name="split/register.html", context={"register_form":form})


def login_request(request):

    if request.user.is_authenticated:
        return redirect("split:feed")

    else:

        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.info(request,f'Welcome back {username}!')
                    return redirect("split:feed")
                else:
                    messages.error(request,"Invalid username or password")
            else:
                messages.error(request,"Invalid username or password")
        form =AuthenticationForm()
        return render(request=request, template_name="split/login.html", context={"login_form":form})


def logout_request(request):

    logout(request)
    messages.info(request,"see you soon.")
    return redirect("split:homepage")


def homepage(request):

    return render(request,'split/home.html')


def feed(request):

    if request.user.is_authenticated:

        return render(request,'split/feed.html')
    
    else:

        return redirect("split:homepage")


def pocket(request):

    if request.user.is_authenticated:

        current_user=get_object_or_404(User,pk=request.user.pk)
        if request.method == 'POST':            
            form = PocketForm(request.POST)            
            if form.is_valid():
                pockets=form.save(commit=False)
                pockets.author = current_user                
                pockets.save()
                form.save_m2m()
                messages.success(request,'Pocket Created')
                return redirect('split:feed')
        else:        
            form=PocketForm()
        return render(request,'split/pocket.html', {'pocket_form':form}) 
        
    else:
        return redirect("split:homepage")


def payment(request):

    if request.user.is_authenticated:

        current_user=get_object_or_404(User,pk=request.user.pk)
        if request.method == 'POST':
            form = PaymentForm(request.POST)
            if form.is_valid():
                payment=form.save(commit=False)
                payment.user = current_user
                payment.save()
                messages.success(request,'Payment Created')
                return redirect('split:feed')
        else:        
            form=PaymentForm()
        return render(request,'split/payment.html', {'payment_form':form}) 
        
    else:
        return redirect("split:homepage")


def charge(request):

    if request.user.is_authenticated:

        current_user=get_object_or_404(User,pk=request.user.pk)
        if request.method == 'POST':
            form = ChargeForm(request.POST)
            if form.is_valid():
                charge=form.save(commit=False)
                charge.user = current_user
                charge.save()
                messages.success(request,'Charge created')
                return redirect('split:feed')
        else:        
            form=ChargeForm()
        return render(request,'split/charge.html', {'charge_form':form}) 
        
    else:
        return redirect("split:homepage")


