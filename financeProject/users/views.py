
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect('home')  # Redirect to a success page.
