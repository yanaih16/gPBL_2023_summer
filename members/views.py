from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def login_user (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("ErrorLogin"))
            return redirect('login')
    else:
        return render(request, "members/login.html")

def logout_user (request):
    logout(request)
    messages.success(request, ("Log out success"))
    return redirect('login')
def register_user (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("registration success"))
            return redirect('login')
    else:
            form = UserCreationForm()

    return render(request, "members/register.html", {'form': form})
