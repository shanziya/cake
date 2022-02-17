from django.shortcuts import render,get_object_or_404,redirect
# from . models import category,Product
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

from .models import Place, District

def cakeprodct(request):
    context = {}
    context['district_list'] = District.objects.all()

    return render(request,"category.html", context)

def register(request):
    context = {}
    context['district_list'] = District.objects.all()

    if request.method == "POST":
        customer_name = request.POST['username']
        customer_email = request.POST['email']

        # address = request.POST['address']
        # phone_number = request.POST['phone_number']
        # district = request.POST['district']
        password = request.POST['password']

        myuser = User.objects.create_user(customer_name,customer_email,password)
        # breakpoint()
        # myuser.address = address
        # myuser.phone_number = phone_number
        # myuser.district = district
        myuser.save()

        messages.success(request,"your account has been successfully created")
        return redirect('cake_shop:login')

    return render(request,'register.html', context)


def login(request):

    context = {}
    context['district_list'] = District.objects.all()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('cake_shop:cake_order_page')
    else:
        form = AuthenticationForm()

    context['form'] = form
    return render(request,'login.html',context)


def cake_order_page(request):
    context = {}
    context['district_list'] = District.objects.all()

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
    context = {}
    context['district_list'] = District.objects.all()
    return render(request, 'cake_list_page.html', context)


def cake_list_places(request):
    context = {}
    context['district_list'] = District.objects.all()

    district = request.GET.get('district', None)
    if district is not None:
        places = Place.objects.filter(district__name__iexact=district)
        context['place_list'] = places

    return render(request, 'cake_list_place.html', context)

