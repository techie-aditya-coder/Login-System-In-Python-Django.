from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "Login/index.html")


def signup(request):
    if request.method == 'POST':
        Username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(Username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created")

        return redirect('signin')
    
    return render(request, "Login/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "Login/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')
        
    return render(request, "Login/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out successfully")
    return redirect('home')
