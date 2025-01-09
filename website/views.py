from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "Username and password are required!")
            return render(request, 'home.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            template_name = 'home.html'
            login(request, user)
            messages.success(request, 'You have been logged in successfully!')
            return render(request, template_name)
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')



def logout_user(request):
    logout(request)
    messages.success(request, "You have a been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

