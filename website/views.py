from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
            return render(request, 'home.html')  # Re-renderiza a página com mensagens de erro
    else:
        return render(request, 'home.html')


def login_user(request):
    pass

def logout_user(request):
    pass


