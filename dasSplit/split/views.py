
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import ChargeForm, PocketForm, NewUserForm,PaymentForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Sum



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

        pockets=Pocket.objects.filter(user__in=[request.user.pk])
        return render(request,'split/feed.html',{'pockets':pockets})
    
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

        
        if request.method == 'POST':
            form = ChargeForm(request.POST)
            if form.is_valid():
                charge=form.save(commit=False)
                charge.save()
                form.save_m2m()
                messages.success(request,'Charge created')
                return redirect('split:feed')
        else:        
            form=ChargeForm()
        return render(request,'split/charge.html', {'charge_form':form}) 
        
    else:
        return redirect("split:homepage")


def show_pocket(request,pocket_id):

    if request.user.is_authenticated:

        pockets = Pocket.objects.get(pk=pocket_id)
        charges= Charge.objects.filter(pocket_id=pocket_id)
        payments= Payment.objects.filter(pocket_id=pocket_id)

        lista= Charge.objects.filter(pocket_id=pocket_id).filter(user__in=[request.user.pk])
        list_value= Charge.objects.filter(pocket_id=pocket_id).filter(user__in=[request.user.pk]).values_list('value')
        list_name=Charge.objects.filter(pocket_id=pocket_id).filter(user__in=[request.user.pk]).values_list('name')


        list_final_value=[]
        list_final_name=[]
        for name in list_name:
            for finalname in name:
                list_final_name.append(finalname)

        count_user_list=[]
        for i in list_final_name:
            count_user=Charge.objects.filter(name=i).values_list("user")
            count_user_list.append(len(count_user)) 

        i=0   
        for value in list_value:
            for finalvalue in value:
                
                finalvalue=(int(finalvalue))//((count_user_list[i]))
                # print(count_user_list[i])
                list_final_value.append(finalvalue)    
                i=i+1

        final=dict(zip(list_final_name,list_final_value))      

        total_payments=Payment.objects.filter(pocket_id=pocket_id).aggregate(Sum('value'))
        total_payments=int(0 if total_payments["value__sum"] is None else total_payments["value__sum"])
        total_charges=Charge.objects.filter(pocket_id=pocket_id).aggregate(Sum('value'))
        total_charges=int(0 if total_charges["value__sum"] is None else total_charges["value__sum"])
        total=total_charges-total_payments

        your_part=sum(final.values()) 

        context={

            'pockets':pockets,
            'charges':charges,
            'payments':payments,
            'total_payments':total_payments,
            'total_charges':total_charges,
            'total':total,
            'lista':lista,
            'final':final,
            'yourpart': your_part,
            

        }  
        return render(request,'split/show_pocket.html',context)
    
    else:

        return redirect("split:homepage")

def update_charge(request,charge_id):  

    if request.user.is_authenticated:
        
        charges=Charge.objects.get(pk=charge_id)
        form=ChargeForm(request.POST or None,instance=charges)
        if form.is_valid():
            form.save()
            return redirect('split:feed')
        return render(request,'split/update_charge.html',{'charge':charges,'form':form})
    else:

        return redirect("split:homepage")
    
def delete_charge(request, charge_id):

    if request.user.is_authenticated:
        
        charges=Charge.objects.get(pk=charge_id)
        print(charges.user)
        if request.user in charges.user.all():
            charges.delete()
            messages.success(request,("Charges deleted!"))                
            return redirect('split:feed')
        else:
            messages.success(request,("You aren't Autorized to delete this charge"))
            return redirect('split:homepage')
        
    else:
        return redirect("split:homepage")




