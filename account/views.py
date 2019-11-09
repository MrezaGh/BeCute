from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from account.models import CustomUser
from barber.models import BarberShop


def landing(request):
    return render(request, 'index.html', context={})


def signup(request):
    if request.POST:

        user = CustomUser.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.type = request.POST['type']
        user.save()

        """create barber shop"""
        if user.type == 'barber':
            shop = BarberShop()
            shop.name = request.POST.get('shop_name')
            shop.barber = user
            shop.save()

        return HttpResponse("signed up successful")

    return render(request, 'registration/signup.html')


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return HttpResponse(f"you are {request.user.username}")
