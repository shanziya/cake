from django.shortcuts import render,get_object_or_404,redirect
# from . models import category,Product
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def cakeprodct(request):
    return render(request,"category.html")

def register(request):
    if request.method == "POST":
        customer_name = request.POST['customer_name']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        district = request.POST['district']
        password = request.POST['password']

        myuser = User.objects.create_user(customer_name,password)
        myuser.address = address
        myuser.phone_number = phone_number
        myuser.district = district

        myuser.save()

        messages.success(request,"your account has been successfully created")
        return redirect('login')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            form.save()

            return redirect('cake_order_page')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request,'login.html',context)


def cake_order_page(request):
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            form.save()

            return redirect('cake_list_page')
    else:
        form = AuthenticationForm()
        context['form'] = form
    return render(request,'cake_order_page.html',context)


def cake_list_page(request):
    return render(request, 'cake_list_page.html')


