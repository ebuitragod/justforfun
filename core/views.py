from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

@login_required(redirect_field_name='justforMagic')
# To decorate the views that we want to protect
# it is suppose it protects the login page 
def secret_page(request):
    return render(request, 'secret_page.html')

class SecretPage(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'secret_page.html'

