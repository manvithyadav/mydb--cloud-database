from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import (
    UserRegistrationForm,
)

from .models import (
    DBUser,
)

APPNAME = 'personal'

# Create your views here.
def renderHomeView(request) :
    context = {}

    if not request.user.is_authenticated :
        return redirect('login')

    return render(request, APPNAME + '/home.html', context)


def renderLoginView(request) :
    context = {}

    if request.user.is_authenticated :
        return redirect('home')

    if request.method == 'POST' :
        # username = request.POST['username']
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)

        if user is None :
            print("invalid credentials")
            return redirect('login')
        
        login(request, user)
    
        return redirect('home')

    else :
        return render(request, APPNAME + '/login.html', context)
    
def renderLogoutView(request) :
    if request.user.is_authenticated :
        logout(request)

    return redirect('home')
    

def renderRegisterView(request) :
    context = {}

    if request.user.is_authenticated :
        return redirect('home')
    
    if request.method == 'POST' :
        userRegistrationForm = UserRegistrationForm(request.POST)

        print("before valid")
        if userRegistrationForm.is_valid() :
            print("form valid")
            name = userRegistrationForm.cleaned_data['name']
            # username = userRegistrationForm.cleaned_data['username']
            # password = userRegistrationForm.cleaned_data['password1']

            user = userRegistrationForm.save()

            dbuser = DBUser.objects.create(
                user=user,
                name=name,
            )

            print(user, dbuser)

            return redirect('login')

        else :
            print("form invalid")
            userRegistrationForm = UserRegistrationForm()
            context['userRegistrationForm'] = userRegistrationForm

            return render(request, APPNAME + '/register.html', context)

    else :
        userRegistrationForm = UserRegistrationForm()
        context['userRegistrationForm'] = userRegistrationForm
        
        # print(userRegistrationForm)

        return render(request, APPNAME + '/register.html', context)
    

def renderProfileView(request) :
    if not request.user.is_authenticated :
        return redirect('login')
    
    context = {}

    return render(request, APPNAME + '/profile.html', context)