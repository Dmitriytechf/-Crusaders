from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.views.generic import TemplateView



class HomeView(TemplateView):
    template_name = 'main/main.html'


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
        
